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

# existing = existing.drop_duplicates(subset='id')
# data = data.drop_duplicates(subset='id')

# data = data.rename(columns={"value": "value_new"})


# combine = pd.concat([existing, data])
combine = pd.concat([existing, data], verify_integrity=True)

print(existing)
print(existing.index.is_unique)
print(data.index.is_unique)

test = uuid.uuid4()

for _ in range(9000000000000000000000000000):
    if uuid.uuid4() == test:
        print("SAME")