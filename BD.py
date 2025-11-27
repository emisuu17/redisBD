import redis

# Conexão com Redis
r = redis.Redis(
    host='redis-12593.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=12593,
    decode_responses=True,
    username="default",
    password="e8IYRU5wGjL9OgzU3bjyy3tuNoTELPXP",
)

# Adicionar tarefas
r.rpush("tarefas", "Estudar Redis")
r.rpush("tarefas", "Fazer exercícios")
r.rpush("tarefas", "Ler um livro")

# Listar todas as tarefas
tarefas = r.lrange("tarefas", 0, -1)
print("Lista de tarefas:", tarefas)

# Remover a primeira tarefa (como se tivesse concluído)
removida = r.lpop("tarefas")
print("Tarefa concluída:", removida)

# Remover uma tarefa específica pelo valor
r.lrem("tarefas", 1, "Ler um livro")

# Listar novamente
tarefas = r.lrange("tarefas", 0, -1)
print("Lista atualizada:", tarefas)
import redis

# Conexão com Redis
r = redis.Redis(
    host='redis-12593.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=12593,
    decode_responses=True,
    username="default",
    password="e8IYRU5wGjL9OgzU3bjyy3tuNoTELPXP",
)

# Adicionar tarefas
r.rpush("tarefas", "Estudar Redis")
r.rpush("tarefas", "Fazer exercícios")
r.rpush("tarefas", "Ler um livro")

# Listar todas as tarefas
tarefas = r.lrange("tarefas", 0, -1)
print("Lista de tarefas:", tarefas)

""""
# Remover a primeira tarefa (como se tivesse concluído)
removida = r.lpop("tarefas")
print("Tarefa concluída:", removida)

# Remover uma tarefa específica pelo valor
r.lrem("tarefas", 1, "Ler um livro")

# Listar novamente
tarefas = r.lrange("tarefas", 0, -1)
print("Lista atualizada:", tarefas)
"""

