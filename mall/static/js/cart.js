/**
 * Created by python on 17-1-9.
 */
function updateCountAndPrice( obj,count ){  //根据数量更新小计
    var price = parseInt(obj.parent().parent().prev().children('em').text()).toFixed();
    var totalprice = price*count;
    obj.parent().parent().next().children('em').text(totalprice);
}


function AllCheckedAndUpdateTotalprice(){
    //根据选中的商品更新总价和商品总数
    var totalcount = parseInt(0);
    var totalprice = parseFloat(0);
    //取出选中的行
    // $('.cart_list_td .col01 input[type="checkbox"]').each(function(){
    //     if($(this).is(':checked')==true){
    //         var count = parseIng($(this).parent().siblings('col06').find('input').val());
    //         var price = parseFloat($(this).parent().siblings('col07').children('em').text());
    //         totalcount = totalcount+count;
    //         totalprice = totalprice+price;
    //     }
    //     $('.settlements .col03 b').text(totalcount);
    //     $('.settlements .col03 em').text(totalprice);
    //
    // });
    var checkboxList = $('.cart_list_td input[type="checkbox"]');
    var checkedList = checkboxList.filter(function () {
        return $(this).prop('checked') == true;
    });

    $(checkedList).each(function(){
        var count = parseInt($(this).parent().siblings('.col06').find('input').val());
        var price = parseFloat($(this).parent().siblings('.col07').children('em').text());
        totalprice = totalprice+price;
        totalcount = totalcount+count;
    });

    $('.settlements .col03 b').text(totalcount);
    $('.settlements .col03 em').text(totalprice);
}

function updateMysql(obj,count){
    var cid = $(obj).parent().parent().siblings('.col01').children('input').attr('name');
    var gcount = count;
    $.get('2/',{"cid":cid,"gnum":gcount});
}

function isCheckUpdateMysql(){
    $('.cart_list_td .col01 input[type="checkbox"]').each(function(){
        var cid = $(this).attr('name');
        var checkobj = parseInt(0);
        if($(this).is(':checked')==true){
            checkobj = 1;
            alert(checkobj);
        }
        else{
            checkobj = 0;
            alert(checkobj);
        }
        $.get('ischeck/',{"cid":cid,"checkobj":checkobj});
    });
}


$(function(){
    AllCheckedAndUpdateTotalprice();
    //页面加载先更新小计
    $('.num_show').each(function(){
        var count = $(this).val();
        updateCountAndPrice($(this),count);

    });

    //点加号增加数量 同时更新小计
    $('.add').click(function(){
        var count = parseInt($(this).next().val());
        count = count +1;
        $(this).next().val(count);
        updateCountAndPrice($(this),count);
        AllCheckedAndUpdateTotalprice();
        updateMysql($(this),count);

    });
    //点减号数量减1 根据数量更新小计
    $('.minus').click(function(){
        var count = parseInt($(this).prev().val());
        if(count>0){
            count = count-1;
            $(this).prev().val(count);
            updateCountAndPrice($(this),count);
            AllCheckedAndUpdateTotalprice();
            updateMysql($(this),count);
        }
    });
    //直接输入数量，更改小计
    $('.cart_list_td .col06 input[type="text"]').change(function(){
        var count = parseInt($(this).val());
        updateCountAndPrice($(this),count);
        AllCheckedAndUpdateTotalprice();
        updateMysql($(this),count);
    });

    //全选效果
    $('.settlements .col01 input[type="checkbox"]').click(function(){
        if($(this).is(':checked')==true){   //点击全部选择
            $('.cart_list_td .col01 input[type="checkbox"]').each(function () {
                $(this).prop('checked',true);
            });
        }
        else{    //取消全选
            $('.cart_list_td .col01 input[type="checkbox"]').each(function(){
                $(this).prop('checked',false)
            });
        }
        AllCheckedAndUpdateTotalprice();
        //判断所有选择框状态，更改数据库
        isCheckUpdateMysql()


        });

    //取消勾选任一行选择框去掉全选对钩
    $('.cart_list_td .col01 input[type="checkbox"]').click(function(){
        if($(this).is(':checked')==false){
            $('.settlements .col01 input[type="checkbox"]').prop('checked',false);
        }
        AllCheckedAndUpdateTotalprice();
        isCheckUpdateMysql();
    });

    //点删除直接从数据库中移除
    $('.cart_list_td .col08 a').click(function(){
        $(this).parent().parent().hide();
        var cid = $(this).parent().siblings('.col01').children('input').attr('name');
        $.get('del/',{"cid":cid});
        AllCheckedAndUpdateTotalprice();
    });




});