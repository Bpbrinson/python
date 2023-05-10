function addCode() {
  let html =
    "<table class='table'><tr><th>Date</th><th>BoA Checkings</th><th>BoA Savings (Vacation)</th><th>BoA Savings Apt./Rainy</th><th>BoA Credit</th><th>BoA Statement</th<th>Amex Credit</th><th>Amex Statement</th><th>Capital One Venture X</th><th>Venture X Statement</th><th>Capital One Savor</th><th>Savor Statement</th><th>Total Credit Debt</th><th>Total Amount</th><th>Etrade</th></tr><tr><td><label for='date'>Date:</label> <input type='date' id='date' name='date[]'></td><td><label for= 'BoA_Checkings'>$$$:</label > <input type='text' id='BoA_Checkings' name='amount[]'></input></td><td><label for= 'BoA Savings (Vacation)'>$$$:</label > <input type='text' id='BoA Savings' name='amount[]'></input></td><td><label for= 'BoA Savings Apt./Rainy'>$$$:</label > <input type='text' id='BoA Savings Apt./Rainy' name='amount[]'></input></td><td><label for= 'BoA_Credit'>$$$:</label > <input type='text' id='BoA_Credit' name='amount[]'></input></td><td><label for= 'BoA_Statememnt'>$$$:</label > <input type='text' id='BoA_Statement' name='amount[]'></input></td><td><label for= 'Amex_Credit'>$$$:</label > <input type='text' id='Amex_Credit' name='amount[]'></input></td><td><label for= 'Amex_Statement'>$$$:</label > <input type='text' id='Amex_Statement' name='amount[]'></input></td><td><label for= 'Capital_One_Venture_X'>$$$:</label > <input type='text' id='Capital_One_Venture_X' name='amount[]'></input></td><td><label for= 'Capital_One_Venture_X_Statement'>$$$:</label > <input type='text' id='Capital_One_Venture_X_Statement' name='amount[]'></input></td><td><label for= 'Capital_One_Savor'>$$$:</label > <input type='text' id='Capital_One_Savor' name='amount[]'></input></td><td><label for= 'Capital_One_Savor_Statement'>$$$:</label > <input type='text' id='Capital_One_Savor_Statement' name='amount[]'></input></td><td><label for= 'Total_Credit_Debt'>$$$:</label > <input type='text' id='Total_Credit_Debt' name='amount[]'></input></td><td><label for= 'Total_Amount'>$$$:</label > <input type='text' id='Total Amount' name='amount[]'></input></td><td><label for= 'Etrade'>$$$:</label > <input type='text' id='Etrade' name='amount[]'></input></td></tr></table>";
  h2.insertAdjacentHTML("beforebegin", html);
}

function addFood() {
  const h2 = document.getElementById("food");
  let html =
    "<table><thead><tr><th>#</th><th>Date</th><th>Meal</th><th>Food</th><th>Amount</th><th>Card Used</th></tr></thead><tbody><tr><td>1</td><td>May 1, 2023</td><td>Breakfast</td><td>Oatmeal</td><td>$3.50</td><td>Visa</td></tr><tr><td>2</td><td>May 1, 2023</td><td>Lunch</td><td>Chicken Caesar Salad</td><td>$9.99</td><td>Mastercard</td></tr></tbody></table>";
  h2.insertAdjacentHTML("beforebegin", html);
}

function viewFood() {
  const h2 = document.getElementById("food");
  let html =
    "<table class='table' id='test'><tr><th>#</th><th style='width:7%''>Date</th><th>#</th><th>Date</th><th>Meal</th><th>Food</th><th>Amount</th><th>Card Used</th></tr>{% for value in data %}<tr><td>{{ value.id }}</td><td>{{ value.date }}</td><td>${{ value.date }}</td><td>${{ value.meal }}</td><td>${{ value.food }}</td><td>${{ value.amount }}</td><td>${{ value.card_used }}</td></tr>{% endfor %}</table>";
  h2.insertAdjacentHTML("beforebegin", html);
}
