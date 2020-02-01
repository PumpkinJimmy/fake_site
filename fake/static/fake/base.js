$(function(){
	result = {};
	var imgs = $(".img-btn");
	for (var i = 0; i < imgs.length; i++){
		imgs[i].onclick = function(){
			if (this.selected) {
				this.selected = false;
				this.style.transform = '';
			}
			else{
				this.selected = true;
				this.style.transform = 'scale(0.9, 0.9)';
			}
		}
	}
	$('#qform').submit(function(e){
		var res = "";
		var qboxs = $(".qbox");
		for (var i = 0; i < qboxs.length; i++){
			if (qboxs[i].getElementsByTagName('img')[0].selected)	
				res += "0";
			else res += "1";
		}
		input = $('<input name="result" value="' + String(res) + '" type="hidden" />');
		$(this).append(input);
	});
});
