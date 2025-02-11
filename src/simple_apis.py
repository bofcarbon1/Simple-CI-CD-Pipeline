from fastapi import FastAPI, HTTPException

# FastAPI app
app = FastAPI()


@app.get("/check_balance/{account_no}")
def check_balance(account_no: int):
    valid_account = 3032158102
    acct_balance = 11257.35
    is_valid_acct = False
    if account_no == valid_account:
        is_valid_acct = True
    if not is_valid_acct:
        return HTTPException(status_code=404, detail="Not a valid account")
    return acct_balance
