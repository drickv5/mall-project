
$(function(){

    $('.add').click(function(){   //点加号增加数量，改变小计
        var count = $(this).next().val();
        count = parseInt(count)+1;  //点加号值加1
        $(this).next().val(count);  //赋值
        var gPrice = parseFloat($(this).parent().parent().prev().children('em').text());  //获取单价
        var totalPrice = gPrice*count;  // 计算小计
        $(this).parent().parent().next().children('em').text(totalPrice);  //向页面传递
        updateGoodsCountAndPrice();
    });


    $('.minus').click(function(){   //点减号减去数量，改变小计
        var count = $(this).prev().val();
        if (count>1){
            count = parseInt(count)-1;   //值减1
            $(this).prev().val(count);  //赋值
            var gPrice = parseFloat($(this).parent().parent().prev().children('em').text());   //获取
            var totalPrice = gPrice*count;
            $(this).parent().parent().next().children('em').html(totalPrice)
        }
        updateGoodsCountAndPrice();
    });

    $('.num_show input').change(function(){   //直接改值，小计发生变化
        var count = $(this).val();
        var gPrice = parseFloat($(this).parent().parent().prev().children('em').text());
        var totalPrice =gPrice*count;
        $(this).parent().parent().next().children('em').text(totalPrice);
        updateGoodsCountAndPrice();
    });

    $('.col08').click(function(){
        $(this).parent().hide();

    });
    $('.settlements input[type="checkbox"]').click(function(){    //全选
        if($(this).is(':checked')==true){
            $('.cart_list_td input[type="checkbox"]').each(function(){
                $(this).prop('checked',true);
            });
            updateGoodsCountAndPrice();
        }

        // else{    //取消全选
        //      $('.cart_list_td input[type="checkbox"]').each(function(){
        //         if($(this).is(':checked')){
        //             $(this).prop('checked',false);
        //         }
        //         else{
        //             $(this).prop('checked',true);
        //         }
        //     });
        //      updateGoodsCountAndPrice();
        // }
    });


});

function updateGoodsCountAndPrice () {
    var totalcount = parseInt(0);
    var totalprice = parseFloat(0);
    var checkList = $('.cart_list_td input[type="checkbox"]').filter(function(){
        return $(this).prop('checked') == true;
    });
    $(checkList).each(function(){
        var count = parseInt($(this).parent().siblings('.col06').find('.num_show').val());
        totalcount = totalcount+count;
        var price = parseFloat($(this).parent().siblings('.col07').find('em').text());
        totalprice = totalprice+price;
    });
    $('.settlements .col03 b').text(totalcount);
    $('.settlements .col03 em').text(totalprice);
}



