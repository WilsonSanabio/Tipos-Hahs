📘 Tipos de Hash
Interface web interativa para explorar os principais algoritmos de hash, com foco educacional e visualmente didático. Cada tipo de hash é apresentado em um card, e ao clicar, um box sobreposto exibe detalhes como tamanho, início e exemplo gerado a partir da string "12345".

🔍 Funcionalidades
Exibição dos principais algoritmos de hash: MD5, SHA-1, SHA-256, SHA-512, bcrypt, argon2id, Base64, entre outros.

Cards interativos com animação ao passar o mouse.

Box modal sobreposto com todas as informações da hash.

Comentário explicativo exibido antes dos dados técnicos.

Layout responsivo e visual limpo.

Separação dos dados em arquivo hash.json para facilitar manutenção.

🚀 Como executar localmente
Clone o repositório:

bash
git clone https://github.com/WilsonSanabio/Tipos-de-Hash.git
Abra o arquivo index.html diretamente no navegador (não é necessário servidor).

Importante: Certifique-se de que o arquivo hash.json esteja na mesma pasta que o index.html.

🗂 Estrutura do projeto
Código
Tipos-de-Hash/
├── index.html         # Página principal
├── estilo.css         # Estilos visuais
├── hash.json          # Dados das hashes
└── README.md          # Documentação do projeto
✏️ Como editar os dados
Para adicionar, remover ou modificar hashes, edite diretamente o arquivo hash.json. Exemplo de estrutura:

json
{
  "hash": "SHA-256",
  "tamanho": 64,
  "inicio": "5994471a",
  "exemplo": "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
}
💡 Sugestões futuras
Botão para copiar o exemplo da hash.

Geração dinâmica de hashes a partir de entrada do usuário.

Exportação para planilha ou integração com Google Sheets.

👨‍💻 Autor
Wilson Sanabio Desenvolvedor web e entusiasta de cibersegurança. Sana/Bios Informática & Consultoria
