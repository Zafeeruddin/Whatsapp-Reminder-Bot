from tasks import add

ans = add.apply_async(args=(4,5), countdown=10)


if ans.ready():
    print(ans.get())