// GA4 with Consent Mode v2 (default denied, granted from localStorage). Same event names as the WordPress site:
// affiliate_click (offers via /go/ or direct shop links), partner_click (Sbalit.cz module). Banner styles live in app.css.
const KEY = 'alk_consent';
export function ga4Head(id: string, pageType: string): string {
  if (!/^G-[A-Z0-9]{6,}$/i.test(id)) return '';
  const src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
  return `<script id="alk-ga4-consent">
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
(function(){var g='denied';try{if(localStorage.getItem('${KEY}')==='1'){g='granted';}}catch(e){}
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:g,functionality_storage:'granted',security_storage:'granted',wait_for_update:500});})();
gtag('js',new Date());
gtag('config','${id}',{page_type:'${pageType}'});
</script>
<script id="alk-ga4">
(function(){var d=0;function go(){if(d)return;d=1;var s=document.createElement('script');s.async=true;s.src=${JSON.stringify(src)};document.head.appendChild(s);}
['pointerdown','keydown','scroll','touchstart'].forEach(function(e){addEventListener(e,go,{once:true,passive:true});});
addEventListener('load',function(){if('requestIdleCallback' in window){requestIdleCallback(go,{timeout:6000});}else{setTimeout(go,6000);}});})();
</script>`;
}
export function ga4Footer(id: string, pageType: string): string {
  if (!/^G-[A-Z0-9]{6,}$/i.test(id)) return '';
  return `<div id="alk-consent" class="alk-consent" style="display:none" role="dialog" aria-live="polite" aria-label="Souhlas s měřením návštěvnosti">
	<p class="alk-consent__t">Měříme návštěvnost, ať víme, které stránky lidem pomáhají. Bez souhlasu měříme jen anonymně, bez cookies.</p>
	<div class="alk-consent__b">
		<button type="button" data-alk-consent="1" class="alk-consent__yes">Souhlasím</button>
		<button type="button" data-alk-consent="0" class="alk-consent__no">Jen nezbytné</button>
		<a href="/ochrana-osobnich-udaju/#cookies" class="alk-consent__l">Více</a>
	</div>
</div>
<script id="alk-ga4-events">
(function(){
	var KEY='${KEY}';
	var PT='${pageType}';
	function store(k,v){try{localStorage.setItem(k,v);}catch(e){}}
	function read(k){try{return localStorage.getItem(k);}catch(e){return null;}}
	var box=document.getElementById('alk-consent');
	if(box&&read(KEY)===null){box.style.display='';}
	if(box){
		box.addEventListener('click',function(e){
			var b=e.target.closest('[data-alk-consent]');
			if(!b){return;}
			var yes=b.getAttribute('data-alk-consent')==='1';
			store(KEY,yes?'1':'0');
			if(window.gtag){gtag('consent','update',{analytics_storage:yes?'granted':'denied'});}
			if(!yes){dropGa();}
			box.style.display='none';
		});
	}
	// Withdrawing consent also removes the GA cookies already set on this domain.
	function dropGa(){
		var parts=location.hostname.split('.'),hosts=[location.hostname];
		if(parts.length>2){hosts.push(parts.slice(-2).join('.'));}
		document.cookie.split(';').forEach(function(c){
			var n=c.split('=')[0].trim();
			if(n!=='_ga'&&n.indexOf('_ga_')!==0&&n!=='_gid'){return;}
			hosts.concat(['.'+hosts[hosts.length-1]]).forEach(function(h){document.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;domain='+h;});
			document.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/';
		});
	}
	// "Change cookie settings" link on the legal pages.
	document.addEventListener('click',function(e){
		var o=e.target&&e.target.closest?e.target.closest('[data-alk-consent-open]'):null;
		if(!o){return;}
		e.preventDefault();
		try{localStorage.removeItem(KEY);}catch(x){}
		if(box){box.style.display='';}
	});
	document.addEventListener('click',function(e){
		if(!e.target||!e.target.closest){return;}
		var a=e.target.closest('a[href]');
		if(!a){return;}
		var pl=a.getAttribute('data-partner-link');
		if(pl){if(window.gtag){gtag('event','partner_click',{partner:pl,link_url:a.href,page_path:location.pathname});}return;}
		var u;try{u=new URL(a.getAttribute('href'),location.href);}catch(err){return;}
		var same=u.host===location.host;
		var viaGo=same&&/^\\/go\\//.test(u.pathname);
		if(!viaGo&&same){return;}
		if(!window.gtag){return;}
		gtag('event','affiliate_click',{
			page_type:PT,
			link_kind:viaGo?'go':'direct',
			partner:a.getAttribute('data-partner')||(viaGo?'':u.host),
			destination:viaGo?u.pathname:u.host,
			context:u.searchParams.get('ctx')||'',
			value:parseInt(a.getAttribute('data-price')||'0',10)||0,
			currency:'CZK'
		});
	},true);
})();
</script>`;
}
