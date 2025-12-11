import redis


r = redis.Redis(
    host='redis-12593.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=12593,
    decode_responses=True,
    username="default",
    password="e8IYRU5wGjL9OgzU3bjyy3tuNoTELPXP",
)

#QUESTÃO 2

# Adicionar jogadores com suas pontuações
r.zadd("ranking", {"Alice": 1500, "Bob": 1200, "Carol": 1800, "David": 900, "Eve": 2000})

# Atualizar pontuação de um jogador (ex: Bob ganhou mais pontos)
r.zincrby("ranking", 300, "Bob")  # Bob passa de 1200 para 1500

# Listar os top 5 jogadores (do maior para o menor)
top5 = r.zrevrange("ranking", 0, 4, withscores=True)

print("Top 5 jogadores:")
for pos, (jogador, pontos) in enumerate(top5, start=1):
    print(f"{pos}. {jogador} - {int(pontos)} pontos")
