from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt_br">
    <head>
    	<meta charset="UTF-8">
    	<title>Faculdade X</title>
    	<style>
                .topnav {
                background-color: #333;
                overflow: hidden;
            }

            .topnav a {
                float: left;
                display: block;
                color: #f2f2f2;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 17px;
            }

            .topnav a:hover {
                background-color: #ddd;
                color: black;
            }

            .topnav a.active {
                background-color: #4CAF50;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>Faculdade X</h1>

        <div class="topnav" id="myTopnav">
            <a href="/aluno/">Aluno</a>
            <a href="/candidato/">Candidato</a>
            <a href="/coordenador/">Coordenador</a>
            <a href="/professor/">Professor</a>

        </div>


    </body>
        <footer>
        <section class="container">
    	   <div>
               <p>Rodrigo Furlaneti</p>
               <p><a href="mailto:rodrigofurlaneti31@hotmail.com">
               rodrigofurlaneti31@hotmail.com</a>.</p>
               </div>
               </section>
               </footer>

        </html>
    """
    return HttpResponse(html)
