'''
curl -X POST -d "username=tope123&password=temmy007" http://127.0.0.1:8000/api/auth/token/

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InRvcGUxMjMiLCJleHAiOjE2MDc2OTE0OTQsImVtYWlsIjoidGVtaUBnbWFpbC5jb20ifQ.w9oZXulPwkF3z8G
TIYl0KCVY1mkaXN9QMEaOyuI70Dc

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InRvcGUxMjMiLCJleHAiOjE2MDc2OTE0OTQsImVtYWlsIjoidGVtaUBnbWFpbC5jb20ifQ.w9oZXulPwkF3z8G
TIYl0KCVY1mkaXN9QMEaOyuI70Dc" http://127.0.0.1:8000/api/comments/

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImZpc2F5b19hZG1pbiIsImV4cCI6MTYwNzY5MDY4MSwiZW1haWwiOiJmaXNheW9hZGVndW5AZ21haWwuY29tIn
0.muztTOtci7pzDhD9vLso5d3ZsQdU554H4Jn6E2uTuas" http://127.0.0.1:8000/api/comments/create/?type=post&slug=hello-world

curl http://127.0.0.1:8000/api/comments/
'''


