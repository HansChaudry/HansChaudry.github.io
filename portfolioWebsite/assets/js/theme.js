document.querySelectorAll('.datepicker').forEach(function(field) {
	var picker = new Pikaday({
		field: field
	});
});

var app = document.getElementById('app');

var typewriter = new Typewriter(app, {
    loop: true,
    delay:50,
    deleteSpeed:5
});

typewriter.typeString("'Hello World!'")
    .pauseFor(1000)
    .deleteAll()
    .pauseFor(500)
    .typeString("'Nice to meet you'")
    .pauseFor(1000)
    .deleteAll()
    .pauseFor(500)
    .typeString("'My name is Hans aka Hansolo'")
    .pauseFor(1000)
    .deleteAll()
    .pauseFor(500)
    .typeString("'I am a student at Hunter College'")
    .pauseFor(1000)
    .deleteAll()
    .pauseFor(500)
    .typeString("'I'm studying Computer Science'")
    .pauseFor(1000)
    .deleteAll()
    .pauseFor(500)
    .typeString("'Thanks for visiting! Hope you Enjoy!'")
    .pauseFor(1000)
    .deleteAll()
    .start();