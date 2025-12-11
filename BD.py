import redis
import time

# Conexão com Redis
r = redis.Redis(
    host='redis-12593.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=12593,
    decode_responses=True,
    username="default",
    password="e8IYRU5wGjL9OgzU3bjyy3tuNoTELPXP",
)

#questão2

# adicionar tarefas
r.rpush("tarefas", "Estudar Redis")
r.rpush("tarefas", "Fazer exercícios")
r.rpush("tarefas", "Ler um livro")

# listar todas as tarefas
tarefas = r.lrange("tarefas", 0, -1)
print("Lista de tarefas:", tarefas)

# Remover a primeira tarefa (como se tivesse concluído)
removida = r.lpop("tarefas")
print("Tarefa concluída:", removida)

# Remover uma tarefa específica pelo valor
r.lrem("tarefas", 1, "Ler um livro")

#questão 3

contador_chave = "pagina:home:visitas"

novo_valor = r.incr(contador_chave)

print(f"A página foi acessada {novo_valor} vezes.")


#questão4

# Nome da chave para o conjunto
usuarios_online = "usuarios:online"

# Função para adicionar usuário quando ele se conecta
def usuario_conectou(user_id):
    r.sadd(usuarios_online, user_id)
    print(f"Usuário {user_id} conectado.")

# Função para remover usuário quando ele sai
def usuario_saiu(user_id):
    r.srem(usuarios_online, user_id)
    print(f"Usuário {user_id} saiu.")

# Função para listar todos os usuários online
def listar_online():
    online = r.smembers(usuarios_online)
    print("Usuários online:", online)

# --- Exemplo de uso ---
usuario_conectou("user_101")
usuario_conectou("user_202")
usuario_conectou("user_303")

listar_online()

usuario_saiu("user_202")

listar_online()


#questão 5

# Função de rate limiting
def permitir_requisicao(user_id, limite=5, janela=60):
    """
    user_id: identificador do usuário
    limite: número máximo de requisições permitidas
    janela: tempo em segundos (ex: 60 = 1 minuto)
    """
    chave = f"rate_limit:{user_id}"
    
    # Incrementa contador
    contagem = r.incr(chave)
    
    # Se for a primeira requisição, define o TTL da chave
    if contagem == 1:
        r.expire(chave, janela)
    
    # Verifica se passou do limite
    if contagem > limite:
        return False, contagem
    return True, contagem

user = "user_101"

for i in range(7):
    permitido, contagem = permitir_requisicao(user)
    if permitido:
        print(f"Requisição {i+1} permitida (total: {contagem})")
    else:
        print(f"Requisição {i+1} bloqueada (total: {contagem})")
    time.sleep(5)  # simula intervalo entre requisições

#questão6

# Conjuntos para um usuário
seguidores_key = "user:101:seguidores"
seguindo_key   = "user:101:seguindo"

# --- Adicionar seguidores ---
r.sadd(seguidores_key, "user_202", "user_303", "user_404")

# --- Adicionar seguindo ---
r.sadd(seguindo_key, "user_202", "user_505", "user_606")

# --- Remover um seguidor ---
r.srem(seguidores_key, "user_404")

# --- Remover alguém que você segue ---
r.srem(seguindo_key, "user_606")

# --- Descobrir amigos em comum (interseção) ---
amigos_comum = r.sinter(seguidores_key, seguindo_key)
print("Amigos em comum:", amigos_comum)

# --- Listar todos os contatos únicos (união) ---
contatos_unicos = r.sunion(seguidores_key, seguindo_key)
print("Todos os contatos únicos:", contatos_unicos)

# --- Descobrir quem você segue que não te segue de volta (diferença) ---
nao_reciprocados = r.sdiff(seguindo_key, seguidores_key)
print("Quem você segue que não te segue de volta:", nao_reciprocados)
