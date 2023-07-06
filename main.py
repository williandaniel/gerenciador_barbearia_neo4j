from neo4j import GraphDatabase
from prettytable import PrettyTable
from menu import *
import pyfiglet

uri = "bolt://localhost:7687"
user = "neo4j"
password = "barbearia"

driver = GraphDatabase.driver(uri, auth=(user, password))

while True:
    print(pyfiglet.figlet_format('Barbearia'))
    res = menuPrincipal()
# ----------------------------EXIBIR-------------------------------------------
    if res['opcao'] == 'Exibir':
        exibir = menuExibir()

        if exibir['opcao'] == 'Clientes':
            with driver.session() as session:
                result = session.run("MATCH (cli:Cliente) OPTIONAL MATCH (cli)-[:CLIENTE_ENDERECO]->(end:Endereco) RETURN cli.cliCod, cli.nome, cli.sobrenome, cli.telefone, cli.cpf, cli.rg, cli.dtnascimento, cli.genero, end.endId ORDER BY toInteger(cli.cliCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            input("Press Enter to continue...")

        if exibir['opcao'] == 'Funcionarios':
            with driver.session() as session:
                result = session.run("MATCH (func:Funcionario)-[:FUNCIONARIO_ENDERECO]->(end:Endereco) RETURN func.funcCod, func.nome, func.sobrenome, func.telefone, func.cpf, func.rg, func.email, func.dtnascimento, func.genero, func.estadocivil, end.endId ORDER BY toInteger(func.funcCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            input("Press Enter to continue...")

        if exibir['opcao'] == 'Endereço':
            with driver.session() as session:
                result = session.run("MATCH (end:Endereco) RETURN end.endId, end.bairro, end.rua, end.numero, end.complemento, end.uf, end.cidade ORDER BY toInteger(end.endId) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            input("Press Enter to continue...")
            
        if exibir['opcao'] == 'Serviços':
            with driver.session() as session:
                result = session.run("MATCH (serv:Servico) RETURN serv.servCod, serv.tiposervico, serv.preco, serv.tempomedio ORDER BY toInteger(serv.servCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            input("Press Enter to continue...")

        if exibir['opcao'] == 'Agendamentos':
            with driver.session() as session:
                result = session.run("MATCH (agen:Agendamento)-[:AGENDAMENTO_FUNCIONARIO]->(func:Funcionario), (agen)-[:AGENDAMENTO_CLIENTE]->(cli:Cliente), (agen)-[:AGENDAMENTO_SERVICO]->(serv:Servico) RETURN agen.agenCod, agen.dataagendamento, agen.hora, agen.situacao, func.funcCod, cli.cliCod, serv.servCod ORDER BY toInteger(agen.agenCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            input("Press Enter to continue...")

        if exibir['opcao'] == 'Voltar':
            continue
# ---------------------------ADICIONAR--------------------------------------------
    if res['opcao'] == 'Adicionar':
            adicionar = menuAdicionar()

            if adicionar['opcao'] == 'Clientes':
                with driver.session() as session:
                    result = session.run("MATCH (cli:Cliente) RETURN MAX(toInteger(cli.cliCod)) AS ultimoCliCod")
                    ultimoCliCod = result.single()["ultimoCliCod"]
                    cliCod = int(ultimoCliCod) + 1

                nome = input("Nome: ")
                sobrenome = input("Sobrenome: ")
                telefone = input("Telefone: ")
                cpf = input("CPF: ")
                if len(cpf) == 0: cpf = 'NULL'
                rg = input("RG: ")
                if len(rg) == 0: rg = 'NULL'
                dtnascimento = input("Data Nascimento (ano-mes-dia): ")
                if len(dtnascimento) == 0: dtnascimento = 'NULL'
                genero = generoC()
                if genero['opcao'] == 'Não Informar': genero['opcao'] = 'NULL'

                with driver.session() as session:
                    result = session.run("CREATE (cli:Cliente {cliCod: $cliCod, nome: $nome, sobrenome: $sobrenome, telefone: $telefone, cpf: $cpf, rg: $rg, dtnascimento: $dtnascimento, genero: $genero})", cliCod=cliCod, nome=nome, sobrenome=sobrenome, telefone=telefone, cpf=cpf, rg=rg, dtnascimento=dtnascimento, genero=genero['opcao'])

                end = endereco()
                if end['opcao'] == True:
                    with driver.session() as session:
                        result = session.run("MATCH (end:Endereco) RETURN MAX(toInteger(end.endId)) AS ultimoEndId")
                        ultimoEndId = result.single()["ultimoEndId"]
                        endId = int(ultimoEndId) + 1

                    bairro = input("Bairro: ")
                    rua = input("Rua: ")
                    numero = input("Número: ")
                    numero = int(numero)
                    complemento = input("Complemento: ")
                    if len(complemento) == 0: complemento = 'NULL'
                    uf = input("UF: ")
                    cidade = input("Cidade: ")

                    with driver.session() as session:
                        result = session.run("CREATE (end:Endereco {endId: $endId, bairro: $bairro, rua: $rua, numero: $numero, complemento: $complemento, uf: $uf, cidade: $cidade})", endId=endId, bairro=bairro, rua=rua, numero=numero, complemento=complemento, uf=uf, cidade=cidade)

                    with driver.session() as session:
                        result = session.run("MATCH (cli:Cliente {cliCod: $cliCod}), (end:Endereco {endId: $endId}) CREATE (cli)-[:CLIENTE_ENDERECO]->(end)", cliCod=cliCod, endId=endId)
                        print("Nó Cliente criado com sucesso!")
                   
                input("Press Enter to continue...")

            if adicionar['opcao'] == 'Funcionarios':
                with driver.session() as session:
                    result = session.run("MATCH (func:Funcionario) RETURN MAX(toInteger(func.funcCod)) AS ultimoFuncCod")
                    ultimoFuncCod = result.single()["ultimoFuncCod"]
                    if ultimoFuncCod is None:
                        funcCod = 1
                    else:
                        funcCod = int(ultimoFuncCod) + 1

                nome = input("Nome: ")
                sobrenome = input("Sobrenome: ")
                telefone = input("Telefone: ")
                cpf = input("CPF: ")
                rg = input("RG: ")
                email = input("E-mail: ")
                dtnascimento = input("Data Nascimento (ano-mes-dia): ")
                gen = generoF()
                estcivil = estadocivil()

                with driver.session() as session:
                    result = session.run("CREATE (func:Funcionario {funcCod: $funcCod, nome: $nome, sobrenome: $sobrenome, telefone: $telefone, cpf: $cpf, rg: $rg, email: $email, dtnascimento: $dtnascimento, genero: $genero, estadocivil: $estadocivil})", funcCod=funcCod, nome=nome, sobrenome=sobrenome, telefone=telefone, cpf=cpf, rg=rg, email=email, dtnascimento=dtnascimento, genero=gen['opcao'], estadocivil=estcivil['opcao'])

                with driver.session() as session:
                    result = session.run("MATCH (end:Endereco) RETURN MAX(toInteger(end.endId)) AS ultimoEndId")
                    ultimoEndId = result.single()["ultimoEndId"]
                    if ultimoFuncCod is None:
                        endId = 1
                    else:
                        endId = int(ultimoEndId) + 1  

                bairro = input("Bairro: ")
                rua = input("Rua: ")
                numero = input("Número: ")
                numero = int(numero)
                complemento = input("Complemento: ")
                if len(complemento) == 0: complemento = 'NULL'
                uf = input("UF: ")
                cidade = input("Cidade: ")
                
                with driver.session() as session:
                        result = session.run("CREATE (end:Endereco {endId: $endId, bairro: $bairro, rua: $rua, numero: $numero, complemento: $complemento, uf: $uf, cidade: $cidade})", endId=endId, bairro=bairro, rua=rua, numero=numero, complemento=complemento, uf=uf, cidade=cidade)

                with driver.session() as session:
                    result = session.run("MATCH (func:Funcionario {funcCod: $funcCod}), (end:Endereco {endId: $endId}) CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end)", funcCod=funcCod, endId=endId)
                    print("Nó Cliente criado com sucesso!")

                input("Press Enter to continue...")


            if adicionar['opcao'] == 'Serviços':
                tiposervico = input("Tipo de Serviço: ")
                preco = int(input("Preço: "))
                tempomedio = int(input("Tempo Médio do Serviço: "))

                with driver.session() as session:
                    result = session.run("MATCH (serv:Servico) RETURN MAX(toInteger(serv.servCod)) AS ultimoServCod")
                    ultimoServCod = result.single()["ultimoServCod"]
                    if ultimoServCod is None:
                        servCod = 1
                    else:
                        servCod = int(ultimoServCod) + 1
                        
                with driver.session() as session:
                    result = session.run("CREATE (serv:Servico {servCod: $servCod, tiposervico: $tiposervico, preco: $preco, tempomedio: $tempomedio})", servCod=servCod, tiposervico=tiposervico, preco=preco, tempomedio=tempomedio)
                    print("Nó Cliente criado com sucesso!")
                input("Press Enter to continue...")

            if adicionar['opcao'] == 'Agendamentos':
                with driver.session() as session:
                    result = session.run("MATCH (agen:Agendamento) RETURN MAX(toInteger(agen.agenCod)) AS ultimoAgenCod")
                    ultimoAgenCod = result.single()["ultimoAgenCod"]
                    if ultimoAgenCod is None:
                        agenCod = 1
                    else:
                        agenCod = int(ultimoAgenCod) + 1
                    
                dataagendamento = input("Informe a Data do Agendamento (ano-mes-dia): ")
                hora = input("Informe a Hora: ")
                funcCod= input("Informe o Codigo do Funcionario: ")
                cliCod = input("Informe o Codigo do Cliente: ")
                servCod = input("Informe o Codigo do servico: ")
                situacao = 'agendado'
                count = 0
                with driver.session() as session:
                    result = session.run("MATCH (func:Funcionario {funcCod: $funcCod}) RETURN toInteger(func.funcCod) as funcCod", funcCod=funcCod)
                    record = result.single()
                    if record is not None and "funcCod" in record:
                        funcCod = record["funcCod"]
                        count = count + 1

                with driver.session() as session:
                    result = session.run("MATCH (cli:Cliente {cliCod: $cliCod}) RETURN toInteger(cli.cliCod) as cliCod", cliCod=cliCod)
                    record = result.single()
                    if record is not None and "cliCod" in record:
                        funcCod = record["cliCod"]
                        count = count + 1

                with driver.session() as session:
                    result = session.run("MATCH (serv:Servico {servCod: $servCod}) RETURN toInteger(serv.servCod) as servCod", servCod=servCod)
                    record = result.single()
                    if record is not None and "servCod" in record:
                        servCod = record["servCod"]
                        count = count + 1

                if count > 0:
                    input("Informe um código existente!")
                    continue
                else:
                    with driver.session() as session:
                        result = session.run(
                            """
                            CREATE (agen:Agendamento {agenCod: $agenCod, dataagendamento: $dataagendamento, hora: $hora, situacao: $situacao})
                            WITH agen
                            MERGE (func:Funcionario {funcCod: $funcCod})
                            MERGE (cli:Cliente {cliCod: $cliCod})
                            MERGE (serv:Servico {servCod: $servCod})
                            MERGE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func)
                            MERGE (agen)-[:AGENDAMENTO_CLIENTE]->(cli)
                            MERGE (agen)-[:AGENDAMENTO_SERVICO]->(serv)
                            """
                            , agenCod=agenCod, dataagendamento=dataagendamento, hora=hora, situacao=situacao, funcCod=funcCod, cliCod=cliCod, servCod=servCod
                        )
                        print("Nó Cliente criado com sucesso!")

                input("Press Enter to continue...")
# -------------------------------REMOVER----------------------------------------    
    if res['opcao'] == 'Remover':
        rem = menuRemover()

        if rem['opcao'] == 'Cliente':
            with driver.session() as session:
                result = session.run("MATCH (cli:Cliente) OPTIONAL MATCH (cli)-[:CLIENTE_ENDERECO]->(end:Endereco) RETURN cli.cliCod, cli.nome, cli.sobrenome, cli.telefone, cli.cpf, cli.rg, cli.dtnascimento, cli.genero, end.endId ORDER BY toInteger(cli.cliCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)

            codcliente = input("Insira o Codigo do Cliente: ")
            cliCod = int(codcliente)
            with driver.session() as session:
                        result = session.run(
                            """
                            MATCH (cli:Cliente {cliCod: $cliCod})-[r1:CLIENTE_ENDERECO]->(end:Endereco)
                            OPTIONAL MATCH (agen:Agendamento)-[r2:AGENDAMENTO_CLIENTE]->(cli)
                            DELETE r1, cli, end, r2, agen
                            """
                            , cliCod=cliCod
                        )
                        print("Nó Cliente removido com sucesso!")

            input("Press Enter to continue...")

        if rem['opcao'] == 'Funcionario':
            with driver.session() as session:
                result = session.run("MATCH (func:Funcionario)-[:FUNCIONARIO_ENDERECO]->(end:Endereco) RETURN func.funcCod, func.nome, func.sobrenome, func.telefone, func.cpf, func.rg, func.email, func.dtnascimento, func.genero, func.estadocivil, end.endId ORDER BY toInteger(func.funcCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)

            codfuncionario = input("Insira o Codigo do Funcionario: ")
            funcCod = int(codfuncionario)
            with driver.session() as session:
                        result = session.run(
                            """
                            MATCH (func:Funcionario {funcCod: $funcCod})-[r1:FUNCIONARIO_ENDERECO]->(end:Endereco)
                            OPTIONAL MATCH (agen:Agendamento)-[r2:AGENDAMENTO_FUNCIONARIO]->(func)
                            DELETE r1, func, end, r2, agen
                            """
                            , funcCod=funcCod
                        )
                        print("Nó Funcionario removido com sucesso!")

            input("Press Enter to continue...")

        if rem['opcao'] == 'Serviço':
            with driver.session() as session:
                result = session.run("MATCH (serv:Servico) RETURN serv.servCod, serv.tiposervico, serv.preco, serv.tempomedio ORDER BY toInteger(serv.servCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)

            codservico = input("Insira o Codigo do Serviço: ")
            servCod = int(codservico)
            with driver.session() as session:
                        result = session.run(
                            """
                            MATCH (serv:Servico {servCod: $servCod})
                            DETACH DELETE serv
                            """
                            , servCod=servCod
                        )
                        print("Nó Serviço removido com sucesso!")

            input("Press Enter to continue...")

        if rem['opcao'] == 'Agendamento':
            with driver.session() as session:
                result = session.run("MATCH (agen:Agendamento)-[:AGENDAMENTO_FUNCIONARIO]->(func:Funcionario), (agen)-[:AGENDAMENTO_CLIENTE]->(cli:Cliente), (agen)-[:AGENDAMENTO_SERVICO]->(serv:Servico) RETURN agen.agenCod, agen.dataagendamento, agen.hora, agen.situacao, func.funcCod, cli.cliCod, serv.servCod ORDER BY toInteger(agen.agenCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)

            codagendamento = input("Insira o Codigo do Agendamento: ")
            agenCod = int(codagendamento)
            with driver.session() as session:
                        result = session.run(
                            """
                            MATCH (agen:Agendamento {agenCod: $agenCod})
                            OPTIONAL MATCH (agen)-[r1:AGENDAMENTO_FUNCIONARIO]->(func:Funcionario)
                            OPTIONAL MATCH (agen)-[r2:AGENDAMENTO_CLIENTE]->(cli:Cliente)
                            OPTIONAL MATCH (agen)-[r3:AGENDAMENTO_SERVICO]->(serv:Servico)
                            DELETE r1, r2, r3, agen   
                            """    
                            , agenCod=agenCod
                        )
                        print("Nó Agendamento removido com sucesso!")

            input("Press Enter to continue...")
# ---------------------------EDITAR------------------------------------
    if res['opcao'] == 'Editar':
        ed = menuEditar()

        if ed['opcao'] == 'Cliente':
            with driver.session() as session:
                result = session.run("MATCH (cli:Cliente) OPTIONAL MATCH (cli)-[:CLIENTE_ENDERECO]->(end:Endereco) RETURN cli.cliCod, cli.nome, cli.sobrenome, cli.telefone, cli.cpf, cli.rg, cli.dtnascimento, cli.genero, end.endId ORDER BY toInteger(cli.cliCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)

            codcliente = input("Insira o Codigo do Cliente: ")
            cliCod = int(codcliente)
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            if len(cpf) == 0: cpf = 'NULL'
            rg = input("RG: ")
            if len(rg) == 0: rg = 'NULL'
            dtnascimento = input("Data Nascimento (ano-mes-dia): ")
            if len(dtnascimento) == 0: dtnascimento = 'NULL'
            genero = generoC()
            if genero['opcao'] == 'Não Informar': genero['opcao'] = 'NULL'

            with driver.session() as session:
                result = session.run(""" MATCH (cli:Cliente {cliCod: $cliCod}) SET cli.nome = $nome, cli.sobrenome = $sobrenome, cli.telefone = $telefone, cli.cpf = $cpf, cli.rg = $rg, cli.dtnascimento = $dtnascimento, cli.genero = $genero """, cliCod=cliCod, nome=nome, sobrenome=sobrenome, telefone=telefone, cpf=cpf, rg=rg, dtnascimento=dtnascimento, genero=genero['opcao'])
                print("Nó Cliente alterado com sucesso!")
            input("Press Enter to continue...")

        if ed['opcao'] == 'Funcionario':
            with driver.session() as session:
                result = session.run("MATCH (func:Funcionario)-[:FUNCIONARIO_ENDERECO]->(end:Endereco) RETURN func.funcCod, func.nome, func.sobrenome, func.telefone, func.cpf, func.rg, func.email, func.dtnascimento, func.genero, func.estadocivil, end.endId ORDER BY toInteger(func.funcCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)

            codfuncionario = input("Insira o Codigo do Funcionario: ")
            funcCod = int(codfuncionario)
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            email = input("E-mail: ")
            dtnascimento = input("Data Nascimento (ano-mes-dia): ")
            gen = generoF()
            estcivil = estadocivil()

            with driver.session() as session:
                result = session.run(""" MATCH (func:Funcionario {funcCod: $funcCod}) SET func.nome = $nome, func.sobrenome = $sobrenome, func.telefone = $telefone, func.cpf = $cpf, func.rg = $rg, func.email = $email, func.dtnascimento = $dtnascimento, func.genero = $genero, func.estadocivil = $estadocivil """, funcCod=funcCod, nome=nome, sobrenome=sobrenome, telefone=telefone, cpf=cpf, rg=rg, email=email, dtnascimento=dtnascimento, genero=gen['opcao'], estadocivil=estcivil['opcao'])
                print("Nó Funcionario alterado com sucesso!")
            input("Press Enter to continue...")

        if ed['opcao'] == 'Endereço':
            editar = editarEndereco()
            if editar['opcao'] == 'Cliente': 
                with driver.session() as session:
                    result = session.run("MATCH (cli:Cliente) OPTIONAL MATCH (cli)-[:CLIENTE_ENDERECO]->(end:Endereco) RETURN cli.cliCod, cli.nome, cli.sobrenome, cli.telefone, cli.cpf, cli.rg, cli.dtnascimento, cli.genero, end.endId ORDER BY toInteger(cli.cliCod) ASC")
                    if result.peek() is None:
                        print("Não houve resultados.")
                    else:
                        table = PrettyTable()
                        table.field_names = result.keys()
                        for record in result:
                            table.add_row(record.values())
                        print(table)
                
                idendereco = input("Insira o ID do Endereço: ")
                endId = int(idendereco)
                with driver.session() as session:
                    result = session.run("MATCH (end:Endereco {endId: $endId}) RETURN end.endId, end.bairro, end.rua, end.numero, end.complemento, end.uf, end.cidade", endId=endId)
                    if result.peek() is None:
                        print("Não houve resultados.")
                    else:
                        table = PrettyTable()
                        table.field_names = result.keys()
                        for record in result:
                            table.add_row(record.values())
                        print(table)

                bairro = input("Bairro: ")
                rua = input("Rua: ")
                numero = input("Número: ")
                numero = int(numero)
                complemento = input("Complemento: ")
                if len(complemento) == 0: complemento = 'NULL'
                uf = input("UF: ")
                cidade = input("Cidade: ")

                with driver.session() as session:
                    result = session.run(""" MATCH (end:Endereco {endId: $endId}) SET end.bairro = $bairro, end.rua = $rua, end.numero = $numero, end.complemento = $complemento, end.uf = $uf, end.cidade = $cidade """, endId=endId, bairro=bairro, rua=rua, numero=numero, complemento=complemento, uf=uf, cidade=cidade)
                    print("Nó Endereço alterado com sucesso!")
            else:
                with driver.session() as session:
                    result = session.run("MATCH (func:Funcionario)-[:FUNCIONARIO_ENDERECO]->(end:Endereco) RETURN func.funcCod, func.nome, func.sobrenome, func.telefone, func.cpf, func.rg, func.email, func.dtnascimento, func.genero, func.estadocivil, end.endId ORDER BY toInteger(func.funcCod) ASC")
                    if result.peek() is None:
                        print("Não houve resultados.")
                    else:
                        table = PrettyTable()
                        table.field_names = result.keys()
                        for record in result:
                            table.add_row(record.values())
                        print(table)
                
                idendereco = input("Insira o ID do Endereço: ")
                endId = int(idendereco)
                with driver.session() as session:
                    result = session.run("MATCH (end:Endereco {endId: $endId}) RETURN end.endId, end.bairro, end.rua, end.numero, end.complemento, end.uf, end.cidade", endId=endId)
                    if result.peek() is None:
                        print("Não houve resultados.")
                    else:
                        table = PrettyTable()
                        table.field_names = result.keys()
                        for record in result:
                            table.add_row(record.values())
                        print(table)
                
                bairro = input("Bairro: ")
                rua = input("Rua: ")
                numero = input("Número: ")
                numero = int(numero)
                complemento = input("Complemento: ")
                if len(complemento) == 0: complemento = 'NULL'
                uf = input("UF: ")
                cidade = input("Cidade: ")
                
                with driver.session() as session:
                    result = session.run(""" MATCH (end:Endereco {endId: $endId}) SET end.bairro = $bairro, end.rua = $rua, end.numero = $numero, end.complemento = $complemento, end.uf = $uf, end.cidade = $cidade """, endId=endId, bairro=bairro, rua=rua, numero=numero, complemento=complemento, uf=uf, cidade=cidade)
                    print("Nó Endereço alterado com sucesso!")

            input("Press Enter to continue...")

        if ed['opcao'] == 'Serviço':
            with driver.session() as session:
                result = session.run("MATCH (serv:Servico) RETURN serv.servCod, serv.tiposervico, serv.preco, serv.tempomedio ORDER BY toInteger(serv.servCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)

            servCod = input("Insira o Codigo do Serviço: ")
            servCod = int(servCod)

            tiposervico = input("Novo Tipo de Serviço: ")
            preco = int(input("Novo Preço: "))
            tempomedio = int(input("Novo Tempo Médio do Serviço: "))

                    
            with driver.session() as session:
                result = session.run("""
                        MATCH (serv:Servico {servCod: $servCod})
                        SET serv.tiposervico = $tiposervico, serv.preco = $preco, serv.tempomedio = $tempomedio
                """, servCod=servCod, tiposervico=tiposervico, preco=preco, tempomedio=tempomedio)
                print("Nó Serviço alterado com sucesso!")
                
            input("Press Enter to continue...")
        
        if ed['opcao'] == 'Agendamento':
            with driver.session() as session:
                result = session.run("MATCH (agen:Agendamento)-[:AGENDAMENTO_FUNCIONARIO]->(func:Funcionario), (agen)-[:AGENDAMENTO_CLIENTE]->(cli:Cliente), (agen)-[:AGENDAMENTO_SERVICO]->(serv:Servico) RETURN agen.agenCod, agen.dataagendamento, agen.hora, agen.situacao, func.funcCod, cli.cliCod, serv.servCod ORDER BY toInteger(agen.agenCod) ASC")
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            
            codagendamento = input("Insira o Codigo do Agendamento: ")
            agenCod = int(codagendamento)

            op = operacaoAgendamento()
            if op['opcao'] == 'Mudar a Situação':
                sit = situacaoAgendamento()
                if sit['opcao'] == 'Cancelado':
                    situacao = 'cancelado'
                    with driver.session() as session:
                        result = session.run(""" MATCH (agen:Agendamento {agenCod: $agenCod}) SET agen.situacao = $situacao """, agenCod=agenCod, situacao=situacao)
                        print("Atributo do Nó Agendamento alterado com sucesso!")
                else:
                    situacao = 'finalizado'
                    with driver.session() as session:
                        result = session.run(""" MATCH (agen:Agendamento {agenCod: $agenCod}) SET agen.situacao = $situacao """, agenCod=agenCod, situacao=situacao)
                        print("Atributo do Nó Agendamento alterado com sucesso!")
            if op['opcao'] == 'Mudar os Dados de Agendamentos':

                dataagendamento = input("Informe a Data do Agendamento (ano-mes-dia): ")
                hora = input("Informe a Hora: ")
                funcCod= input("Informe o Codigo do Funcionario: ")
                cliCod = input("Informe o Codigo do Cliente: ")
                servCod = input("Informe o Codigo do servico: ")
           
                with driver.session() as session:
                    result = session.run("""
                            MATCH (agen:Agendamento {agenCod: $agenCod})
                            SET agen.dataagendamento = $dataagendamento, agen.hora = $hora, agen.funcCod = $funcCod, agen.cliCod = $cliCod, agen.servCod = $servCod
                    """, agenCod=agenCod, dataagendamento=dataagendamento, hora=hora, funcCod=funcCod, cliCod=cliCod, servCod=servCod)
                    print("Nó Serviço alterado com sucesso!")
            input("Press Enter to continue...")
                
# -----------------------------RELATORIOS------------------------------------------
    if res['opcao'] == 'Relatórios':
        rel = menuRelatorios()
        
        if rel['opcao'] == 'Total Ganho por Funcionário':
            with driver.session() as session:
                result = session.run("""
                        MATCH (agen:Agendamento)-[:AGENDAMENTO_FUNCIONARIO]->(func:Funcionario), (agen:Agendamento)-[:AGENDAMENTO_SERVICO]->(serv:Servico)
                        WHERE agen.situacao = 'finalizado'
                        WITH func.funcCod AS codfuncionario, func.nome AS nomefuncionario, func.sobrenome AS sobrenomefuncionario, agen.agenCod AS codAgendamento, serv.preco AS precoservico
                        RETURN codfuncionario, nomefuncionario, sobrenomefuncionario, sum(toFloat(precoservico)) AS valorTotal
                        ORDER BY valorTotal DESC
                    """)
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            input("Press Enter to continue...")

        if rel['opcao'] == 'Quantidade de Cancelamentos por Cliente':
            with driver.session() as session:
                result = session.run("""
                        MATCH (cli:Cliente)
                        OPTIONAL MATCH (cli)-[:CLIENTE_ENDERECO]->(end:Endereco)
                        MATCH (agen:Agendamento)-[:AGENDAMENTO_CLIENTE]->(cli)
                        MATCH (agen)-[:AGENDAMENTO_SERVICO]->(serv:Servico)
                        WHERE agen.situacao = 'cancelado'
                        WITH cli.cliCod AS codcliente, cli.nome AS nomecliente, cli.sobrenome AS sobrenomecliente, end.bairro AS bairro, serv.preco AS precoservico, agen.agenCod AS codAgendamento
                        RETURN codcliente, nomecliente, sobrenomecliente, bairro, sum(toFloat(precoservico)) AS valorTotal, COUNT(codAgendamento) AS quantidade
                        ORDER BY quantidade DESC, codcliente
                    """)
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            input("Press Enter to continue...")

        if rel['opcao'] == 'Futuros Ganhos por Funcionário':
            with driver.session() as session:
                result = session.run("""
                        MATCH (agen:Agendamento)-[:AGENDAMENTO_FUNCIONARIO]->(func:Funcionario), (agen:Agendamento)-[:AGENDAMENTO_SERVICO]->(serv:Servico)
                        WHERE agen.situacao = 'agendado'
                        WITH func.funcCod AS codfuncionario, func.nome AS nomefuncionario, func.sobrenome AS sobrenomefuncionario, agen.agenCod AS codAgendamento, serv.preco AS precoservico
                        RETURN codfuncionario, nomefuncionario, sobrenomefuncionario, sum(toFloat(precoservico)) AS valorTotal
                        ORDER BY valorTotal DESC    
                    """)
                if result.peek() is None:
                    print("Não houve resultados.")
                else:
                    table = PrettyTable()
                    table.field_names = result.keys()
                    for record in result:
                        table.add_row(record.values())
                    print(table)
            input("Press Enter to continue...")
# -----------------------------------------------------------------------       
    if res['opcao'] == 'Sair':
        break