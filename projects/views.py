from django.shortcuts import render

from django.db import connection
from django.http import JsonResponse

def get_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM local")
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'nombre': row[1],
                'ubicacion': row[2]
            })
    return JsonResponse({'data': data})