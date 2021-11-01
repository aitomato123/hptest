/* 食品伙伴网   http://www.foodmate.net/ 狂三少 */
function m(i) { try { Dd(i).className = 'tab_on'; } catch(e) {} }
function s(i) { try { Dd(i).className = 'side_b'; } catch(e) {} }
function v(i) { if(Dd(i).className == 'side_a') Dd(i).className = 'side_c'; }
function t(i) { if(Dd(i).className == 'side_c') Dd(i).className = 'side_a'; }
function c(i) {
	Dd('menu_'+i).className = 'layui-nav-item layui-nav-itemed';
	window.scrollTo(0,0);
}
function nav_c(i) {
	console.log('a');
	for(var j = 0; j < 6; j++) {
		if(j == i) {
			$('#menu_'+j).hasClass("layui-nav-itemed")?($('#menu_'+j).className = 'layui-nav-item'):($('#menu_'+j).className = 'layui-nav-item layui-nav-itemed');
		} else {
			if($('#menu_'+j).length>0)Dd('menu_'+j).className = 'layui-nav-item';
		}
	}
	window.scrollTo(0,0);
}

function oh(o) {
	if(o.className == 'side_h') {
		Dh('side');o.className = 'side_s';
		set_local('m_side', 'Y');
	} else {
		Ds('side');o.className = 'side_h';
		set_local('m_side', 'N');
	}
}