from pathlib import Path

vault = Path.home() / "brodye-vault"
print(vault)

notes = vault.rglob("*.md")
count = 0

for note in notes:
    count = count + 1

print("Total notes:", count)
