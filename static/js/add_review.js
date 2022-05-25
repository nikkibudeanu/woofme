const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.review-form')


const handleSelect = (selection) => {
    switch (selection) {
        case 'first': {
            one.classList.add('selected')
            two.classList.remove('selected')
            three.classList.remove('selected')
            four.classList.remove('selected')
            five.classList.remove('selected')
            return

        }
        case 'second': {
            one.classList.add('selected')
            two.classList.add('selected')
            three.classList.remove('selected')
            four.classList.remove('selected')
            five.classList.remove('selected')
            return

        }
        case 'third': {
            one.classList.add('selected')
            two.classList.add('selected')
            three.classList.add('selected')
            four.classList.remove('selected')
            five.classList.remove('selected')
            return

        }
        case 'fourth': {
            one.classList.add('selected')
            two.classList.add('selected')
            three.classList.add('selected')
            four.classList.add('selected')
            five.classList.remove('selected')
            return

        }
        case 'fifth': {
            one.classList.add('selected')
            two.classList.add('selected')
            three.classList.add('selected')
            four.classList.add('selected')
            five.classList.add('selected')
            return

        }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1
    } else if (stringValue === 'second') {
        numericValue = 2
    } else if (stringValue === 'third') {
        numericValue = 3
    } else if (stringValue === 'fourth') {
        numericValue = 4
    } else if (stringValue === 'fifth') {
        numericValue = 5
    } else {
        numericValue = 0
    }
    return numericValue
}


const arr = [one, two, three, four, five]

arr.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelect(event.target.id)

}))


arr.forEach(item => item.addEventListener('click', (event) => {
    const val = event.target.id
    console.log(val)

    const val_num = getNumericValue(val)
    console.log(val_num)
    form.rating.value = val_num
    console.log(form.rating.value)
})) 