

tags=["ai", "ml", "python", "ml", "dl", "ai"]

seen= set()
duplicate= set()

for item in tags:
    if item in seen:
        duplicate.add(item)
    else:
        seen.add(item)

print("duplicate : " ,list(duplicate))

