MATCH (n) DETACH DELETE n;

CREATE (serv:Servico {servCod: 1, tiposervico: 'Cabelo', preco: 80, tempomedio: 60});
CREATE (serv:Servico {servCod: 2, tiposervico: 'Barba', preco: 50, tempomedio: 30});
CREATE (serv:Servico {servCod: 3, tiposervico: 'Corte e Barba', preco: 120, tempomedio: 90});


CREATE (func:Funcionario {funcCod: 1, nome: 'Carlos', sobrenome: 'Aguiar', telefone: '(47) 3998-1150', cpf: '67899879833', rg: '676865689', email: 'carlos.aguiar@gmail.com', dtnascimento: '1988-03-27', genero: 'Masculino', estadocivil: 'Separado'});
CREATE (func:Funcionario {funcCod: 2, nome: 'Ana', sobrenome: 'Silva', telefone: '(47) 1234-5678', cpf: '12345678901', rg: '987654321', email: 'ana.silva@gmail.com', dtnascimento: '1990-08-15', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 3, nome: 'Mário', sobrenome: 'Souza', telefone: '(47) 9876-5432', cpf: '98765432109', rg: '123456789', email: 'mario.souza@gmail.com', dtnascimento: '1995-05-10', genero: 'Masculino', estadocivil: 'Casado'});
CREATE (func:Funcionario {funcCod: 4, nome: 'Juliana', sobrenome: 'Ribeiro', telefone: '(47) 4567-8901', cpf: '45678901234', rg: '876543210', email: 'juliana.ribeiro@gmail.com', dtnascimento: '1992-11-22', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 5, nome: 'Ricardo', sobrenome: 'Lima', telefone: '(47) 9876-1234', cpf: '56789012345', rg: '765432109', email: 'ricardo.lima@gmail.com', dtnascimento: '1985-07-03', genero: 'Masculino', estadocivil: 'Casado'});
CREATE (func:Funcionario {funcCod: 6, nome: 'Camila', sobrenome: 'Fernandes', telefone: '(47) 5555-5555', cpf: '09876543210', rg: '432109876', email: 'camila.fernandes@gmail.com', dtnascimento: '1993-04-18', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 7, nome: 'Fernando', sobrenome: 'Santos', telefone: '(47) 1111-1111', cpf: '01234567890', rg: '321098765', email: 'fernando.santos@gmail.com', dtnascimento: '1991-09-07', genero: 'Masculino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 8, nome: 'Laura', sobrenome: 'Martins', telefone: '(47) 2222-2222', cpf: '23456789012', rg: '543210987', email: 'laura.martins@gmail.com', dtnascimento: '1994-12-30', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 9, nome: 'Pedro', sobrenome: 'Oliveira', telefone: '(47) 3333-3333', cpf: '34567890123', rg: '654321098', email: 'pedro.oliveira@gmail.com', dtnascimento: '1990-02-12', genero: 'Masculino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 10, nome: 'Luiza', sobrenome: 'Almeida', telefone: '(47) 4444-4444', cpf: '45678901234', rg: '765432109', email: 'luiza.almeida@gmail.com', dtnascimento: '1995-06-25', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 11, nome: 'Paulo', sobrenome: 'Gomes', telefone: '(47) 5555-5555', cpf: '56789012345', rg: '876543210', email: 'paulo.gomes@gmail.com', dtnascimento: '1987-10-08', genero: 'Masculino', estadocivil: 'Casado'});
CREATE (func:Funcionario {funcCod: 12, nome: 'Beatriz', sobrenome: 'Pereira', telefone: '(47) 6666-6666', cpf: '67890123456', rg: '987654321', email: 'beatriz.pereira@gmail.com', dtnascimento: '1993-03-15', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 13, nome: 'Gustavo', sobrenome: 'Mendes', telefone: '(47) 7777-7777', cpf: '78901234567', rg: '876543210', email: 'gustavo.mendes@gmail.com', dtnascimento: '1991-01-20', genero: 'Masculino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 14, nome: 'Carolina', sobrenome: 'Rocha', telefone: '(47) 8888-8888', cpf: '89012345678', rg: '765432109', email: 'carolina.rocha@gmail.com', dtnascimento: '1994-08-05', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 15, nome: 'André', sobrenome: 'Silveira', telefone: '(47) 9999-9999', cpf: '90123456789', rg: '654321098', email: 'andre.silveira@gmail.com', dtnascimento: '1989-06-10', genero: 'Masculino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 16, nome: 'Mariana', sobrenome: 'Campos', telefone: '(47) 0000-0000', cpf: '01234567890', rg: '321098765', email: 'mariana.campos@gmail.com', dtnascimento: '1992-12-17', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 17, nome: 'Henrique', sobrenome: 'Ferreira', telefone: '(47) 1111-1111', cpf: '12345678901', rg: '432109876', email: 'henrique.ferreira@gmail.com', dtnascimento: '1990-09-22', genero: 'Masculino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 18, nome: 'Isabella', sobrenome: 'Viana', telefone: '(47) 2222-2222', cpf: '23456789012', rg: '543210987', email: 'isabella.viana@gmail.com', dtnascimento: '1993-02-01', genero: 'Feminino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 19, nome: 'Lucas', sobrenome: 'Santana', telefone: '(47) 3333-3333', cpf: '34567890123', rg: '654321098', email: 'lucas.santana@gmail.com', dtnascimento: '1988-07-14', genero: 'Masculino', estadocivil: 'Solteiro'});
CREATE (func:Funcionario {funcCod: 20, nome: 'Gabriela', sobrenome: 'Costa', telefone: '(47) 4444-4444', cpf: '45678901234', rg: '765432109', email: 'gabriela.costa@gmail.com', dtnascimento: '1994-05-27', genero: 'Feminino', estadocivil: 'Solteiro'});

CREATE (cli:Cliente {cliCod: 1, nome: 'Rafael', sobrenome: 'Gomes', telefone: '(47) 4445-4544', cpf: '45678501264', rg: '764432901', dtnascimento: '1994-05-29', genero: 'Masculino'});
CREATE (cli:Cliente {cliCod: 2, nome: 'Carolina', sobrenome: 'Silva', telefone: '(47) 1234-5678', cpf: '12345678901', rg: '987654321', dtnascimento: '1990-08-15', genero: 'Feminino'});
CREATE (cli:Cliente {cliCod: 3, nome: 'Marcelo', sobrenome: 'Santos', telefone: '(47) 9876-5432', cpf: '98765432109', rg: '123456789', dtnascimento: '1995-05-10', genero: 'Masculino'});
CREATE (cli:Cliente {cliCod: 4, nome: 'Juliana', sobrenome: 'Ribeiro', telefone: '(47) 4567-8901', cpf: '45678901234', rg: '876543210', dtnascimento: '1992-11-22', genero: 'Feminino'});
CREATE (cli:Cliente {cliCod: 5, nome: 'Rodrigo', sobrenome: 'Lima', telefone: '(47) 9876-1234', cpf: '56789012345', rg: '765432109', dtnascimento: '1985-07-03', genero: 'Masculino'});
CREATE (cli:Cliente {cliCod: 6, nome: 'Camila', sobrenome: 'Fernandes', telefone: '(47) 5555-5555', cpf: '09876543210', rg: '432109876', dtnascimento: '1993-04-18', genero: 'Feminino'});
CREATE (cli:Cliente {cliCod: 7, nome: 'Fernanda', sobrenome: 'Santos', telefone: '(47) 1111-1111', cpf: '01234567890', rg: '321098765', dtnascimento: '1991-09-07', genero: 'Feminino'});
CREATE (cli:Cliente {cliCod: 8, nome: 'Lucas', sobrenome: 'Martins', telefone: '(47) 2222-2222', cpf: '23456789012', rg: '543210987', dtnascimento: '1994-12-30', genero: 'Masculino'});
CREATE (cli:Cliente {cliCod: 9, nome: 'Pedro', sobrenome: 'Oliveira', telefone: '(47) 3333-3333', cpf: '34567890123', rg: '654321098', dtnascimento: '1990-02-12', genero: 'Masculino'});
CREATE (cli:Cliente {cliCod: 10, nome: 'Luiza', sobrenome: 'Almeida', telefone: '(47) 4444-4444', cpf: '45678901234', rg: '765432109', dtnascimento: '1995-06-25', genero: 'Feminino'});
CREATE (cli:Cliente {cliCod: 11, nome: 'Paulo', sobrenome: 'Gomes', telefone: '(47) 5555-5555', cpf: '56789012345', rg: '876543210', dtnascimento: '1987-10-08', genero: 'Masculino'});
CREATE (cli:Cliente {cliCod: 12, nome: 'Beatriz', sobrenome: 'Pereira', telefone: '(47) 6666-6666', cpf: '67890123456', rg: '987654321', dtnascimento: '1993-03-15', genero: 'Feminino'});

CREATE (end:Endereco {endId: 1, bairro: 'Costa e Silva', rua: 'Almirante Jaceguay', numero: 111, complemento: 'Apt 101 Bloco F', uf: 'SC', cidade: 'Joinville'});
CREATE (end:Endereco {endId: 2, bairro: 'Centro', rua: 'Rua do Comércio', numero: 456, complemento: 'Apt 202 Bloco C', uf: 'SP', cidade: 'São Paulo'});
CREATE (end:Endereco {endId: 3, bairro: 'Boa Vista', rua: 'Rua das Flores', numero: 789, complemento: 'Casa 2', uf: 'RS', cidade: 'Porto Alegre'});
CREATE (end:Endereco {endId: 4, bairro: 'Centro', rua: 'Avenida Central', numero: 321, complemento: 'Casa 4', uf: 'RJ', cidade: 'Rio de Janeiro'});
CREATE (end:Endereco {endId: 5, bairro: 'Jardim das Acácias', rua: 'Rua dos Ipês', numero: 987, complemento: 'Casa 7', uf: 'MG', cidade: 'Belo Horizonte'});
CREATE (end:Endereco {endId: 6, bairro: 'Centro', rua: 'Rua do Comércio', numero: 654, complemento: 'Apt 102', uf: 'BA', cidade: 'Salvador'});
CREATE (end:Endereco {endId: 7, bairro: 'Jardim América', rua: 'Avenida das Palmeiras', numero: 543, complemento: 'Casa 1', uf: 'GO', cidade: 'Goiânia'});
CREATE (end:Endereco {endId: 8, bairro: 'Centro', rua: 'Rua Principal', numero: 879, complemento: 'Casa 8', uf: 'PR', cidade: 'Curitiba'});
CREATE (end:Endereco {endId: 9, bairro: 'Vila Nova', rua: 'Rua das Oliveiras', numero: 456, complemento: 'NULL', uf: 'SC', cidade: 'Florianópolis'});
CREATE (end:Endereco {endId: 10, bairro: 'Centro', rua: 'Avenida Central', numero: 789, complemento: 'NULL', uf: 'SP', cidade: 'Campinas'});
CREATE (end:Endereco {endId: 11, bairro: 'Boa Vista', rua: 'Rua das Flores', numero: 123, complemento: 'Casa 1', uf: 'RS', cidade: 'Caxias do Sul'});
CREATE (end:Endereco {endId: 12, bairro: 'Centro', rua: 'Rua do Comércio', numero: 987, complemento: 'NULL', uf: 'RJ', cidade: 'Niterói'});
CREATE (end:Endereco {endId: 13, bairro: 'Jardim das Acácias', rua: 'Rua dos Ipês', numero: 321, complemento: 'NULL', uf: 'MG', cidade: 'Uberlândia'});
CREATE (end:Endereco {endId: 14, bairro: 'Centro', rua: 'Rua do Comércio', numero: 654, complemento: 'NULL', uf: 'BA', cidade: 'Feira de Santana'});
CREATE (end:Endereco {endId: 15, bairro: 'Jardim América', rua: 'Avenida das Palmeiras', numero: 987, complemento: 'NULL', uf: 'GO', cidade: 'Anápolis'});
CREATE (end:Endereco {endId: 16, bairro: 'Centro', rua: 'Rua Principal', numero: 543, complemento: 'NULL', uf: 'PR', cidade: 'Londrina'});
CREATE (end:Endereco {endId: 17, bairro: 'Vila Nova', rua: 'Rua das Oliveiras', numero: 879, complemento: 'NULL', uf: 'SC', cidade: 'Itajaí'});
CREATE (end:Endereco {endId: 18, bairro: 'Centro', rua: 'Avenida Central', numero: 456, complemento: 'NULL', uf: 'SP', cidade: 'Santos'});
CREATE (end:Endereco {endId: 19, bairro: 'Boa Vista', rua: 'Rua das Flores', numero: 789, complemento: 'Apto 301', uf: 'RS', cidade: 'Pelotas'});
CREATE (end:Endereco {endId: 20, bairro: 'Centro', rua: 'Rua do Comércio', numero: 123, complemento: 'NULL', uf: 'RJ', cidade: 'Nova Iguaçu'});
CREATE (end:Endereco {endId: 21, bairro: 'Jardim das Acácias', rua: 'Rua dos Ipês', numero: 987, complemento: 'NULL', uf: 'MG', cidade: 'Juiz de Fora'});
CREATE (end:Endereco {endId: 22, bairro: 'Centro', rua: 'Rua do Comércio', numero: 654, complemento: 'NULL', uf: 'BA', cidade: 'Vitória da Conquista'});
CREATE (end:Endereco {endId: 23, bairro: 'Jardim América', rua: 'Avenida das Palmeiras', numero: 321, complemento: 'NULL', uf: 'GO', cidade: 'Anápolis'});
CREATE (end:Endereco {endId: 24, bairro: 'Centro', rua: 'Rua Principal', numero: 987, complemento: 'NULL', uf: 'PR', cidade: 'Maringá'});
CREATE (end:Endereco {endId: 25, bairro: 'Vila Nova', rua: 'Rua das Oliveiras', numero: 456, complemento: 'NULL', uf: 'SC', cidade: 'Balneário Camboriú'});
CREATE (end:Endereco {endId: 26, bairro: 'Centro', rua: 'Avenida Central', numero: 789, complemento: 'NULL', uf: 'SP', cidade: 'Ribeirão Preto'});
CREATE (end:Endereco {endId: 27, bairro: 'Boa Vista', rua: 'Rua das Flores', numero: 123, complemento: 'Casa 1', uf: 'RS', cidade: 'Passo Fundo'});
CREATE (end:Endereco {endId: 28, bairro: 'Centro', rua: 'Rua do Comércio', numero: 987, complemento: 'NULL', uf: 'RJ', cidade: 'Petrópolis'});
CREATE (end:Endereco {endId: 29, bairro: 'Jardim das Acácias', rua: 'Rua dos Ipês', numero: 321, complemento: 'NULL', uf: 'MG', cidade: 'Governador Valadares'});
CREATE (end:Endereco {endId: 30, bairro: 'Centro', rua: 'Rua do Comércio', numero: 654, complemento: 'NULL', uf: 'BA', cidade: 'Ilhéus'});
CREATE (end:Endereco {endId: 31, bairro: 'Jardim América', rua: 'Avenida das Palmeiras', numero: 987, complemento: 'NULL', uf: 'GO', cidade: 'Goiânia'});
CREATE (end:Endereco {endId: 32, bairro: 'Centro', rua: 'Rua Principal', numero: 543, complemento: 'NULL', uf: 'PR', cidade: 'Curitiba'});


CREATE (agen:Agendamento {agenCod: 1, dataagendamento: '2023-04-21', hora: '08:00:00', situacao: 'agendado'});
CREATE (agen:Agendamento {agenCod: 2, dataagendamento: '2023-04-22', hora: '09:30:00', situacao: 'agendado'});
CREATE (agen:Agendamento {agenCod: 3, dataagendamento: '2023-04-23', hora: '10:45:00', situacao: 'finalizado'});
CREATE (agen:Agendamento {agenCod: 4, dataagendamento: '2023-04-24', hora: '14:15:00', situacao: 'finalizado'});
CREATE (agen:Agendamento {agenCod: 5, dataagendamento: '2023-04-25', hora: '16:30:00', situacao: 'cancelado'});
CREATE (agen:Agendamento {agenCod: 6, dataagendamento: '2023-04-26', hora: '10:00:00', situacao: 'agendado'});
CREATE (agen:Agendamento {agenCod: 7, dataagendamento: '2023-04-27', hora: '11:30:00', situacao: 'agendado'});
CREATE (agen:Agendamento {agenCod: 8, dataagendamento: '2023-04-28', hora: '15:00:00', situacao: 'finalizado'});
CREATE (agen:Agendamento {agenCod: 9, dataagendamento: '2023-04-29', hora: '09:00:00', situacao: 'agendado'});
CREATE (agen:Agendamento {agenCod: 10, dataagendamento: '2023-04-30', hora: '13:30:00', situacao: 'finalizado'});



MATCH (func:Funcionario {funcCod: 1}), (end:Endereco {endId: 1})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 2}), (end:Endereco {endId: 2})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 3}), (end:Endereco {endId: 3})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 4}), (end:Endereco {endId: 4})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 5}), (end:Endereco {endId: 5})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 6}), (end:Endereco {endId: 6})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 7}), (end:Endereco {endId: 7})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 8}), (end:Endereco {endId: 8})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 9}), (end:Endereco {endId: 9})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 10}), (end:Endereco {endId: 10})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 11}), (end:Endereco {endId: 11})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 12}), (end:Endereco {endId: 12})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 13}), (end:Endereco {endId: 13})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 14}), (end:Endereco {endId: 14})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 15}), (end:Endereco {endId: 15})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 16}), (end:Endereco {endId: 16})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 17}), (end:Endereco {endId: 17})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 18}), (end:Endereco {endId: 18})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 19}), (end:Endereco {endId: 19})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);
MATCH (func:Funcionario {funcCod: 20}), (end:Endereco {endId: 20})
CREATE (func)-[:FUNCIONARIO_ENDERECO]->(end);



MATCH (cli:Cliente {cliCod: 1}), (end:Endereco {endId: 21})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 2}), (end:Endereco {endId: 22})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 3}), (end:Endereco {endId: 23})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 4}), (end:Endereco {endId: 24})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 5}), (end:Endereco {endId: 25})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 6}), (end:Endereco {endId: 26})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 7}), (end:Endereco {endId: 27})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 8}), (end:Endereco {endId: 28})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 9}), (end:Endereco {endId: 29})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 10}), (end:Endereco {endId: 30})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 11}), (end:Endereco {endId: 31})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);
MATCH (cli:Cliente {cliCod: 12}), (end:Endereco {endId: 32})
CREATE (cli)-[:CLIENTE_ENDERECO]->(end);

MATCH (agen:Agendamento {agenCod: 1}), (func:Funcionario {funcCod: 1}), (cli:Cliente {cliCod: 1}), (serv:Servico {servCod: 1})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
       (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
       (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 2}), (func:Funcionario {funcCod: 1}), (cli:Cliente {cliCod: 2}), (serv:Servico {servCod: 2})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
       (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
       (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 3}), (func:Funcionario {funcCod: 1}), (cli:Cliente {cliCod: 3}), (serv:Servico {servCod: 3})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
       (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
       (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 4}), (func:Funcionario {funcCod: 2}), (cli:Cliente {cliCod: 4}), (serv:Servico {servCod: 2})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
       (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
       (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 5}), (func:Funcionario {funcCod: 2}), (cli:Cliente {cliCod: 5}), (serv:Servico {servCod: 3})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
       (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
       (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 6}), (func:Funcionario {funcCod: 2}), (cli:Cliente {cliCod: 6}), (serv:Servico {servCod: 1})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
       (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
       (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 7}), (func:Funcionario {funcCod: 2}), (cli:Cliente {cliCod: 7}), (serv:Servico {servCod: 3})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
       (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
       (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 8}), (func:Funcionario {funcCod: 3}), (cli:Cliente {cliCod: 8}), (serv:Servico {servCod: 2})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
       (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
       (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 9}), (func:Funcionario {funcCod: 4}), (cli:Cliente {cliCod: 9}), (serv:Servico {servCod: 3})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
        (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
        (agen)-[:AGENDAMENTO_SERVICO]->(serv);
MATCH (agen:Agendamento {agenCod: 10}), (func:Funcionario {funcCod: 5}), (cli:Cliente {cliCod: 10}), (serv:Servico {servCod: 2})
CREATE (agen)-[:AGENDAMENTO_FUNCIONARIO]->(func),
        (agen)-[:AGENDAMENTO_CLIENTE]->(cli),
        (agen)-[:AGENDAMENTO_SERVICO]->(serv);