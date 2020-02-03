$(function(){
	result = {};
	var boxs = $(".qbox");
	// 绑定图片点击事件
	for (var i = 0; i < boxs.length; i++)
	{
		boxs[i].option = "n"; //null
		var btns = $(boxs[i]).find(".img-btn");
		btns[0].selected = false;
		btns[1].selected = true;
		btns[0].qbox = boxs[i];
		btns[0].obtn = btns[1];
		btns[0].option = 'a';
		btns[1].qbox = boxs[i];
		btns[1].obtn = btns[0];
		btns[1].option = 'b';
		var handler = function(){
			if (this.selected) {
				this.selected = false;
				this.className = "img-btn";
				this.qbox.option = "n";
			}
			else{
				this.selected = true;
				this.className += " selected"
				this.obtn.selected = false;
				this.obtn.className = "img-btn";
				this.qbox.option = this.option;
			}
		}
		btns[0].onclick = handler;
		btns[1].onclick = handler;
	}
	// 提交，验证完成情况
	$('#qform').submit(function(e){
		var res = "";
		var qboxs = $(".qbox");
		for (var i = 0; i < qboxs.length; i++){
			if (qboxs[i].option == 'n')
			{
				e.preventDefault();
				alert("问题" + (i + 1) + "未回答");
				return;
			}

			res += qboxs[i].option
		}
		input = $('<input name="result" value="' + String(res) + '" type="hidden" />');
		$(this).append(input);
	});
});
