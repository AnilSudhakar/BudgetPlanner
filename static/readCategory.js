    $(document).ready(function () {

    let arrData = [];

  	// Fill the first dropdown with data.
    $.getJSON('../../static/stylesheet/category.json', function (data) {


        let arr_category = [];

        $.each(data, function (index, value) {
            arr_category.push(value.Type);
            arrData = data;
        });

        // Remove duplicates.
        arr_category = Array.from(new Set (arr_category));

        // ref (https://www.encodedna.com/javascript/remove-duplicates-in-javascript-array-using-es6-set-and-from.htm)

        $.each(arr_category, function (index, value) {
            // Fill the first dropdown.
            $('#main_category').append('<option value="' + value + '">' + value + '</option>');
        });

    });

    $('#main_category').change(function () {
        let type = this.options[this.selectedIndex].value;

        let filterData = arrData.filter(function(value) {
            return value.Type === type;
        });

        $('#sub_category')
            .empty()
            .append('<option value=""> Select Sub-category </option>');

        $.each(filterData, function (index, value) {
            // Now, fill the second dropdown list with category names.
            $('#sub_category').append('<option value="' + value.Name + '">' + value.Name + '</option>');
        });

    });
  });