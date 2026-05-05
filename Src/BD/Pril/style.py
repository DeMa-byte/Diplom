* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #f4f4f4;
    padding: 20px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

h1 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
}

.stats {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
}

.stat-card {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    flex: 1;
    text-align: center;
}

.stat-card h3 {
    color: #666;
    margin-bottom: 10px;
}

.stat-card .number {
    font-size: 32px;
    font-weight: bold;
    color: #007bff;
}

.menu {
    display: flex;
    gap: 10px;
    margin-bottom: 30px;
    flex-wrap: wrap;
}

.btn {
    display: inline-block;
    padding: 10px 20px;
    background: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    cursor: pointer;
    border: none;
}

.btn-danger {
    background: #dc3545;
}

.btn-warning {
    background: #ffc107;
    color: #333;
}

.btn:hover {
    opacity: 0.8;
}

table {
    width: 100%;
    background: white;
    border-collapse: collapse;
    margin-top: 20px;
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background: #007bff;
    color: white;
}

tr:hover {
    background: #f5f5f5;
}

form {
    background: white;
    padding: 20px;
    border-radius: 8px;
    max-width: 500px;
}

input, select, textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

label {
    font-weight: bold;
    display: block;
    margin-bottom: 5px;
}