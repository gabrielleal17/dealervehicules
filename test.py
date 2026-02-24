import psycopg2

try:
    # Copia aquí tu cadena de conexión exacta
    conn = psycopg2.connect("postgresql://postgres.votjisdewytppsljubiy:pruebabbase123@aws-0-us-west-2.pooler.supabase.com:6543/postgres?sslmode=require")
    print("✅ ¡Conexión exitosa a Supabase!")
    conn.close()
except Exception as e:
    print(f"❌ Error todavía: {e}")

    