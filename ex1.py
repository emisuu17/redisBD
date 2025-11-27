import redis

# Conectar ao Redis (localhost, porta padrão 6379)
r = redis.Redis(host='localhost', port=6379, db=0)

# Adicionar tarefas
r.rpush("tarefas", "Estudar Redis")
r.rpush("tarefas", "Fazer exercícios")

# Listar tarefas
print(r.lrange("tarefas", 0, -1))

# Remover a primeira tarefa
r.lpop("tarefas")
