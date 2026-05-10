# simulacao_malwere
simulação de keylogger e ransomware

## Ransomware
É um tipo de software malicioso que sequestra todos os dados de determinado dispositivo e os criptografa, exigindo resgate através de um pagamento para devolver o acesso. Porém, na maioria dos casos, os dados não são devolvidos mesmo após o pagamento.

### Etapas de funcionamento
- Gerar chave: Foi utilizado o pacote Fernet da biblioteca cryptography para gerar uma chave.
- Criptografar arquivos da máquina alvo: A chave criada na etapa anterior foi utlizada no calculo matemático para realizar a criptografia dos arquivos da máquina alvo.
- Localizar arquivos: Cria-se uma lista vazia para armazenar os arquivos que devem ser criptografados, os arquivos são localizados a partir da biblioteca os e armazenados com o uso de um loop for.
- executar arquivo: Chama-se a função de gerar chave e carregar chave, e, em seguida, a função encontrar arquivos é chamada (a busca dos arquivos ocorre a partir da constante diretório), após isso, executa-se um loop para criptografar todos os arquivos presentes na lista.
