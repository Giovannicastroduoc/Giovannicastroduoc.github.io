// Obtener el elemento con la clase 'hotel-price' y formatear su contenido como número con separador de miles
var elem = document.querySelector('.hotel-price');
elem.innerHTML = parseFloat(elem.innerHTML).toLocaleString();

// Inicializar el slider con la clase 'slider'
const slider = document.querySelector('.slider');
M.Slider.init(slider, {
    indicators: true,
    height: 400,
    transition: 500,
    interval: 6000
});

// Obtener los elementos relacionados con el calendario
var cal = document.querySelector('.calendar');
var checkin = document.querySelector('.datepicker');
var checkout = document.querySelector('.datepicker2');

// Configurar las fechas mínima y máxima para el calendario
var date = new Date();
var maxDate = new Date(date.setMonth(date.getMonth() + 12));

// Inicializar el datepicker para el checkin
var instance = M.Datepicker.init(checkin, {
    container: cal,
    defaultDate: new Date(),
    setDefaultDate: true,
    minDate: new Date(),
    maxDate: maxDate,
    yearRange: [new Date().getFullYear(), new Date().getFullYear() + 1],
    onClose: checkDates,
});

// Calcular la fecha mínima para el checkout basada en el checkin seleccionado
var x = new Date(document.querySelector('input[name="checkin"]').value);
var minCheckOut = new Date(x.setDate(x.getDate() + 1));
var maxCheckOut = new Date(date.setMonth(date.getMonth() + 12));

// Inicializar el datepicker para el checkout
var instance2 = M.Datepicker.init(checkout, {
    container: cal,
    defaultDate: minCheckOut,
    setDefaultDate: true,
    minDate: minCheckOut,
    maxDate: maxCheckOut,
    yearRange: [new Date().getFullYear(), new Date().getFullYear() + 1],
});

// Inicializar los elementos select
var elems = document.querySelectorAll('select');
M.FormSelect.init(elems, {});

// Calcular el precio total basado en las opciones seleccionadas
function createPrice() {
    var x = document.querySelector('input[name="checkin"]').value;
    var y = document.querySelector('input[name="checkout"]').value;
    var days = Math.floor((Date.parse(y) - Date.parse(x)) / 86400000);
    var originalPrice = parseFloat(document.querySelector('.original-price').value);
    var elem = document.querySelector('.hotel-price');
    var room = document.querySelector('select[name="room"').value;
    var adult = document.querySelector('select[name="adult"').value;
    var child = document.querySelector('select[name="child"').value;
    var newPrice = originalPrice * room +
        Math.floor(originalPrice * (adult - 1) * 0.5) +
        Math.floor(originalPrice * child / 4) +
        Math.floor(originalPrice * (days - 1) / 3);
    elem.innerHTML = parseFloat(newPrice).toLocaleString();
    document.querySelector('#days').value = days;
}

// Verificar las fechas seleccionadas y actualizar el datepicker del checkout si es necesario
function checkDates() {
    var x = new Date(document.querySelector('input[name="checkin"]').value);
    var minCheckOut = new Date(x.setDate(x.getDate() + 1));
    var y = new Date(document.querySelector('input[name="checkout"]').value);

    var options = {
        container: cal,
        minDate: minCheckOut,
        maxDate: maxCheckOut,
        yearRange: [new Date().getFullYear(), new Date().getFullYear() + 1],
    };

    if (x >= y) {
        options.defaultDate = minCheckOut;
        options.setDefaultDate = true;
    }

    M.Datepicker.init(checkout, options);
    var a = minCheckOut.toDateString().split(" ");
    var b = `${a[1]} ${a[2]}, ${a[3]}`;
    document.querySelector('input[name="checkout"]').value = b;
    createPrice();
}
