from django.http import Http404
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Team, Person
from .serializers import PersonSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=['POST'])
    def add_people_to_team(self, request, pk=None):
        team = self.get_object()
        people_ids = request.data.get('people_ids', [])

        if people_ids:
            people_to_add = Person.objects.filter(id__in=people_ids)
            people_to_add.update(team=team)
            return Response({'detail': f'{len(people_to_add)} persons added to team {team.id}'},
                            status=status.HTTP_200_OK)

        return Response({'detail': 'Please provide a list of "people_ids" to add to the team'},
                        status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'])
    def remove_people_from_team(self, request, pk=None):
        try:
            team = self.get_object()
            people_ids = request.data.get('people_ids', [])

            if people_ids:
                people_to_remove = Person.objects.filter(team=team, id__in=people_ids)
                people_to_remove.update(team=None)
                return Response({'detail': f'{people_to_remove.count()} persons removed from team ID:{team.id}'},
                                status=status.HTTP_200_OK)

            people_to_remove = Person.objects.filter(team=team)
            people_to_remove.update(team=None)
            return Response({'detail': f'All persons removed from the team ID:{team.id}'}, status=status.HTTP_200_OK)

        except Http404:
            return Response({'detail': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
