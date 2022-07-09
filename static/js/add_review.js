// all stars
var one = document.getElementById('first');
var two = document.getElementById('second');
var three = document.getElementById('third');
var four = document.getElementById('fourth');
var five = document.getElementById('fifth');

var form = document.querySelector('.review-form');


// get the stars to hover and add or delete selected class
var handleSelect = (selection) => {
    switch (selection) {
        case 'first': {
            one.classList.add('selected');
            two.classList.remove('selected');
            three.classList.remove('selected');
            four.classList.remove('selected');
            five.classList.remove('selected');
            return;

        }
        case 'second': {
            one.classList.add('selected');
            two.classList.add('selected');
            three.classList.remove('selected');
            four.classList.remove('selected');
            five.classList.remove('selected');
            return;

        }
        case 'third': {
            one.classList.add('selected');
            two.classList.add('selected');
            three.classList.add('selected');
            four.classList.remove('selected');
            five.classList.remove('selected');
            return;

        }
        case 'fourth': {
            one.classList.add('selected');
            two.classList.add('selected');
            three.classList.add('selected');
            four.classList.add('selected');
            five.classList.remove('selected');
            return;

        }
        case 'fifth': {
            one.classList.add('selected');
            two.classList.add('selected');
            three.classList.add('selected');
            four.classList.add('selected');
            five.classList.add('selected');
            return;

        }
    }
};

// convert string value to numeric value 
var getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1;
    } else if (stringValue === 'second') {
        numericValue = 2;
    } else if (stringValue === 'third') {
        numericValue = 3;
    } else if (stringValue === 'fourth') {
        numericValue = 4;
    } else if (stringValue === 'fifth') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
};


var arr = [one, two, three, four, five];


// event listener when hover on rating stars

arr.forEach(item => item.addEventListener('click', (event) => {
    handleSelect(event.target.id);


}));

// convert string value to numeric value

arr.forEach(item => item.addEventListener('click', (event) => {
    var val = event.target.id;
    var num_value = getNumericValue(val);
    form.rating.value = num_value;
}));

