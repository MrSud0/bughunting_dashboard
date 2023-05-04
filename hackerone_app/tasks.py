import requests
from celery import shared_task
from django.conf import settings
from .models import Program, Report, User, Activity

HACKERONE_API_BASE_URL = 'https://api.hackerone.com/v1'

def get_hackerone_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.HACKERONE_API_TOKEN}',
    }

@shared_task
def fetch_hackerone_programs():
    url = f'{HACKERONE_API_BASE_URL}/programs'
    headers = get_hackerone_headers()
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        programs_data = response.json()['data']
        for program_data in programs_data:
            attributes = program_data['attributes']
            program, _ = Program.objects.update_or_create(
                program_id=program_data['id'],
                defaults={
                    'name': attributes['name'],
                    'url': attributes['url'],
                    'handle': attributes['handle'],
                    'created_at': attributes['created_at'],
                    'updated_at': attributes['updated_at'],
                }
            )

@shared_task
def fetch_reports_for_program(program_id):
    url = f'{HACKERONE_API_BASE_URL}/programs/{program_id}/reports'
    headers = get_hackerone_headers()
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        reports_data = response.json()['data']
        for report_data in reports_data:
            attributes = report_data['attributes']
            reporter_data = report_data['relationships']['reporter']['data']
            reporter, _ = User.objects.update_or_create(
                user_id=reporter_data['id'],
                defaults={
                    'username': reporter_data['attributes']['username'],
                    'name': reporter_data['attributes']['name'],
                    'created_at': reporter_data['attributes']['created_at'],
                    'updated_at': reporter_data['attributes']['updated_at'],
                }
            )
            program = Program.objects.get(program_id=program_id)
            report, _ = Report.objects.update_or_create(
                report_id=report_data['id'],
                defaults={
                    'title': attributes['title'],
                    'vulnerability_information': attributes['vulnerability_information'],
                    'created_at': attributes['created_at'],
                    'updated_at': attributes['updated_at'],
                    'first_program_activity_at': attributes['first_program_activity_at'],
                    'last_program_activity_at': attributes['last_program_activity_at'],
                    'state': attributes['state'],
                    'substate': attributes['substate'],
                    'severity_rating': attributes['severity_rating'],
                    'program': program,
                    'reporter': reporter,
                }
            )
