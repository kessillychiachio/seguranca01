import zipfile

zip_filename = 'mensagem.zip'
wordlist_filename = 'rockyou.txt'

with zipfile.ZipFile(zip_filename) as zf:
  with open(wordlist_filename, 'r', encoding='latin-1') as f:
    for line in f:
      password = line.strip()
      try:
        zf.extractall(pwd=password.encode('utf-8'))
        print(f'[+]Senha encontrada: {password}')
        break
      except:
        print(f'[-]Tentativa falhou: {password}')