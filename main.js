let person = {};

person.sleep = function() {
  console.log('Sleeping !!!');
};
person.eat = () => console.log('Eating!!');
person.pray = () => console.log('Praying Salah');
person.code = () => 'Coding JS';

// Calling
person.sleep();
person.eat();
person.pray();
console.log(person.code());

const user = {
  name: 'Hassan'
};

const userWithAge = {
  ...user,
  Age: 29
};

console.log(userWithAge);
