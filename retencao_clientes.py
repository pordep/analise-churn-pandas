import pandas as pd
import numpy as np
from datetime import datetime

data = {
    'cliente_id': [12345, 34567, 5678],
    'data_ultima_compra': ['2025-08-12', '2026-01-13', '2026-02-02'],
    'total_gasto': [500, 700, 300],
    'plano': ['Prata', 'Ouro', 'Bronze']
}

df = pd.DataFrame(data)

df['data_ultima_compra'] = pd.to_datetime(df['data_ultima_compra'])

agora = datetime.now()
dias_sem_comprar = (agora - df['data_ultima_compra']).dt.days


df['status'] = np.where(dias_sem_comprar > 90, 'CRÍTICO', 'OK')

print(df)