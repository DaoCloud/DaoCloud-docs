//这个脚本的作用是让所有的链接在新页面打开。
//由于markdown不能给a元素加target属性，且把所有的链接用html重写太麻烦，所以就用这个办法。
$(function(){
	var myAnchors=$("#body a")
	for (var i = myAnchors.length - 1; i >= 0; i--) {
		$(myAnchors[i]).attr('target','_blank')
	};
})
