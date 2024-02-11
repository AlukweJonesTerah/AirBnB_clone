# univaserly unique identifiers
import uuid

import pandas as pd

data = pd.DataFrame({
    # "id": [1, 2, 3, 4, 5, 6],
    "id": [uuid.uuid4() for _ in range(6)],
    "value": [40, 20, 10, 20, 30, 30],
    "value2": [1, 1, 1, 0, 0, 1]
})

data = data.set_index("id")

existing = pd.read_csv("existing_data.csv")
existing = existing.set_index("id")

combine = pd.concat([existing, data])
combine = pd.concat([existing, data], verify_integrity=True)
print(existing)