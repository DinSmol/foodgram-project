function onClickHandler(){
	var tag_br=document.getElementById("breakfast").checked;
	var tag_ln=document.getElementById("lunch").checked;
	var tag_dn=document.getElementById("dinner").checked;
	window.history.pushState({}, document.title, "");
	var url = window.location.href;    
	if (url.indexOf('?') > -1){
		url = window.location.origin + window.location.pathname; 
		url += '?param=1'
	}
	else{
		url += '?param=1'
	}
	if (tag_br){
		url += '&breakfast=1'
	}
	else{
		url += '&breakfast=0'   
	}
	if (tag_ln){
		url += '&lunch=1'
	}
	else{
		url += '&lunch=0'   
	}
	if (tag_dn){
		url += '&dinner=1'
	}
	else{
		url += '&dinner=0'   
	}
	window.location.href = url;
	
	}
