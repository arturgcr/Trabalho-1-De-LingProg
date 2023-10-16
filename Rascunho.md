FEITO:

- Fluxograma básico
- Menu
- Cadastro
- Tags
- Tabela de horários
- Selecionar tipo de reunião quero criar



FALTA:

- Código
    - Visualizar horários individualmente
    - Dar match em horários
    - Terminar de estilizar o aplicativo
    - Tratamento de erro (não deixar avançar sem completar tudo pedido e etc)

- Apresentação
- Relatório

- Oracle, MySQL, Microsoft SQL Server, PostgreSQL, IBM DB2



<!-- Tela para cadastro -->

<!-- Conf iniciais e ja chama arquivo do css para estilizar a pagina-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/styleCadastro.css"> <!-- Use o mesmo arquivo CSS da tela de login -->
</head>

<body>
    <div class="login-container"> <!-- editar dps no css-->
        <div class="sidebar"> <!-- editar dps no css-->
            <h2>Cadastro</h2>
                
            <!-- CONFIGURAÇÃO PARA CARGOS -->
            <div class="input-group"> <!-- editar dps no css - Para cargos -->
                <label for="cargos">Cargos:</label> <!-- Mostra na tela "Cargos"-->
                <form action="#" method="POST"> <!-- Define se marcado = POST -->
                    <table border="1">

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Trainne</td> 
                            <td><input type="checkbox" name="Trainee" value="Trainee"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Membro</td> 
                            <td><input type="checkbox" name="Membro" value="Membro"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Lider</td> 
                            <td><input type="checkbox" name="Lider" value="Lider"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Gestão</td> 
                            <td><input type="checkbox" name="Gestão" value="Gestão"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Indiferente</td> 
                            <td><input type="checkbox" name="Indiferente" value="Indiferente"></td>
                        </tr>

                    </div>
                </div>
            </div>

            <!-- CONFIGURAÇÃO PARA PROJETOS -->
            <div class="input-group"> <!-- editar dps no css - Para Projetos -->
                <label for="Projetos">Projetos:</label> <!-- Mostra na tela "Cargos"-->
                <form action="#" method="POST"> <!-- Define se marcado = POST -->
                    <table border="1">

                        <tr>  <!-- Defino linhas os Projetos -->
                            <td>Gestão</td> 
                            <td><input type="checkbox" name="Gestão" value="Gestão"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Líderes</td> 
                            <td><input type="checkbox" name="Líderes" value="Líderes"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Combate Grande</td> 
                            <td><input type="checkbox" name="Combate Grande" value="Combate Grande"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Combate Pequeno</td> 
                            <td><input type="checkbox" name="Combate Pequeno" value="Combate Pequeno"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Seguidor</td> 
                            <td><input type="checkbox" name="Seguidor" value="Seguidor"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Trekking</td> 
                            <td><input type="checkbox" name="Trekking" value="Trekking"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Mini</td> 
                            <td><input type="checkbox" name="Mini" value="Mini"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>3kg</td> 
                            <td><input type="checkbox" name="3kg" value="3kg"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Lego</td> 
                            <td><input type="checkbox" name="Lego" value="Lego"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Marketing</td> 
                            <td><input type="checkbox" name="Marketing" value="Marketing"></td>
                        </tr>

                        <tr>  <!-- Defino linhas os cargos -->
                            <td>Administração</td> 
                            <td><input type="checkbox" name="Administração" value="Administração"></td>
                        </tr>

                    </div>
                </div>
            </div>




        </div>
        <div class="main-content">
            <h1>Cadastro Geral</h1>
            <form action="#" method="POST">
                <div class="input-group">
                    <label for="nome">Nome:</label>
                    <input type="text" id="nome" name="nome" required>
                </div>
                <div class="input-group">
                    <label for="email">E-mail:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                {% if request.method == 'POST' and erroEmail %}
                <ul>
                    {% for mensagem in erroEmail.mensagens %}
                    <li style="color: red;">{{ mensagem }}</li>
                    {% endfor %}
                </ul>
                {% endif %}
                <div class="input-group">
                    <label for="senha">Senha:</label>
                    <input type="password" id="senha" name="senha" required>
                </div>
                {% if request.method == 'POST' and erroSenha %}
                <ul>
                    {% for mensagem in erroSenha.mensagens %}
                    <li style="color: red;">{{ mensagem }}</li>
                    {% endfor %}
                </ul>
                {% endif %}
                {% if request.method == 'POST' and erroCampos %}
                <ul>
                    {% for mensagem in erroCampos.mensagens %}
                    <li style="color: red;">{{ mensagem }}</li>
                    {% endfor %}
                </ul>
                {% endif %}
                <div class="input-group">
                    <label for="confirmar_senha">Confirmar Senha:</label>
                    <input type="password" id="confirmar_senha" name="confirmar_senha" required>
                </div>
                <button type="submit" class="botao-cadastrar">Cadastrar</button>            </form>
            <p class="mt-3 text-center">Já tem uma conta? <a href="/Login">Faça o login</a></p>
        </div>

        </table>
        <br>
        <input type="submit" value="Finalizar">
        <button type="button" onclick="voltar()">Voltar</button>

        <script>
            function voltar() {
                window.history.back();
            }
        </script>
        
    </form>
</body>
</html>