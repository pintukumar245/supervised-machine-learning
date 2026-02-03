db.createCollection("students");
db.students.insertMany([
  { name: "Alice", age: 21, depaertment: "Computer Science" },
  { name: "Bob", age: 22, major: "Mathematics" },
  { name: "Charlie", age: 23, major: "Physics" }
]);
db.createCollection("courses");
db.courses.insertMany([
  { subject: "Database Systems", credits: 3 },
    { subject: "Calculus", credits: 4 },
    { subject: "Quantum Mechanics", credits: 3 }
]);