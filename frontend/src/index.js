import App from '@components/App';
import './index.css';

window.app = new App({
	target: document.querySelector('#app'),
	hydrate: true
});

if (process.env.NODE_ENV === 'production') {

	// Service Worker registration
	if ('serviceWorker' in navigator) {
		navigator.serviceWorker.register('/sw.js');
	}
}
