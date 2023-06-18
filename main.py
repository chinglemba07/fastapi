from fastapi import FastAPI

data = [
    {
    "name": "chinglemba",
    "address": "sega road",
    "age": 32,
    "sex": "m"
    },
    {
        "name": "ashani",
        "address": "sega road",
        "age": 26,
        "sex": "f"
    },
    {
        "name": "ajay",
        "address": "thangmeiband",
        "age": 23,
        "sex": "m"
    }
]

# Step 2: Create a FastAPI application instance
app = FastAPI()

# Step 3: Define FastAPI endpoints
@app.get('/items/{name}')
async def get_items(name):
    flag = 0
    for nm in data:
        if name == nm['name']:
            flag = 1
            if nm['sex'] == 'm':
                sex = 'he'
            else:
                sex = 'she'
            return f"{name} is from {nm['address']} and {sex} is {nm['age']} years old"
    if flag == 0:
        return {'message': 'No match found'}



# Step 4: Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
