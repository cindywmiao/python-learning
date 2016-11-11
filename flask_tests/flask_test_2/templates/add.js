function add()
{
    var adder1 = Number(document.form1.adder1.value);
    var adder2 = Number(document.form1.adder2.value);
    var result = adder1 + adder2;
    document.form1.result.value = result;
}