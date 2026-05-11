# simulacao_malwere
simulação de keylogger e ransomware

## Ransomware
É um tipo de software malicioso que sequestra todos os dados de determinado dispositivo e os criptografa, exigindo resgate através de um pagamento para devolver o acesso. Porém, na maioria dos casos, os dados não são devolvidos mesmo após o pagamento.

### Etapas de funcionamento
#### criptografador
- Gerar chave: Foi utilizado o pacote Fernet da biblioteca cryptography para gerar uma chave.
- Criptografar arquivos da máquina alvo: A chave criada na etapa anterior foi utlizada no calculo matemático para realizar a criptografia dos arquivos da máquina alvo.
- Localizar arquivos: Cria-se uma lista vazia para armazenar os arquivos que devem ser criptografados, os arquivos são localizados a partir da biblioteca os e armazenados com o uso de um loop for.
- executar arquivo: Chama-se a função de gerar chave e carregar chave, e, em seguida, a função encontrar arquivos é chamada (a busca dos arquivos ocorre a partir da constante diretório), após isso, executa-se um loop para criptografar todos os arquivos presentes na lista.
#### descriptografador
- Carregar chave: A chave presente no arquivo chave.key foi lida pelo programa.
- Descriptografar arquivo: A chave criada anteriormente é utilizada no calculo matemático para descriptografar os dados criptografados e retorná-los aos seus arquivos de origem.
- Encontrar arquivos: Segue a mesma lógica do ransomware, criando uma lista e adicionando os arquivos do diretório que foi criptografado.
- executar arquivo: Chama a função carregar chave e a atribui a variável chave, depois, percorre os arquivos da lista e os descriptografa utilizando a chave.

## Keylogger
É um tipo de software malicioso que monitora e captura tudo que é digitado no teclado da máquina alvo, capturando informações sensíveis como senhas, mensagens e dados confidenciais, enviando as informações capturadas até o atacante sem o conhecimento da vítima.
### Etapas de funcionamento
- Capturar teclas digitadas: Foi utilizado o módulo keyboard da biblioteca pynput para realizar a captura de teclas digitadas. O código captura a tecla e tenta adicioná-la à string de caracteres digitados (log) pela máquina alvo. Ademais, quando o sistema lança AttributeError, ocorre tratamento de exceção.
- Enviar email: É definido um timer que, a cada 60 segundos, envia a string atual de caracteres acumulados para o e-mail de destino a partir do e-mail de origem. Após a definição do timer, a função tenta realizar uma conexão com o servidor SMTP, com parâmetros como senha do e-mail de origem e nome do e-mail de origem.

## Maneiras de se defender
- Manter o sistema operacional atualizado
- usar antivírus com proteção em tempo real
- Possuir um firewall bem configurado
- Usar autenticação de dois fatores (2FA)
- Não abrir ou baixar arquivos suspeitos

## Aviso legal
Este repositório contém código criado exclusivamente para fins educacionais. Os programas simulam comportamentos maliciosos e devem ser testados somente em ambiente controlado.

É proibido utilizar o código em dispositivos sem autorização, para fins maliciosos ou contra terceiros.
