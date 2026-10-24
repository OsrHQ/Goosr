# ميزان الجولة · Round Scale

حاسبة لايف لجولات **Up or Down 5m** (طالع أو نازل في 5 دقايق) على BTC وETH وBNB.

- تاخذ السعر لايف من Binance (أكثر من مرة في الثانية) وسعر البداية لكل جولة.
- تقدّر احتمال Up (طالع) وDown (نازل) من بعد السعر عن سعر البداية والوقت الباقي وحركة السوق في آخر ساعة.
- توضح كم بتربح وكم بتخسر قبل أي صفقة، وتقارن مع أسعار التطبيق.
- فيها حدود جلسة (حد وقف، هدف، وقت) تقول لك وقّف لما توصلها.

ما تعرف وين بيروح السعر، ولا أحد يعرف. هي أداة حساب، مو توصية.

The page is a single static `index.html` (no build step). It reads public market data from `data-stream.binance.vision` (WebSocket) and `data-api.binance.vision` (REST). Everything the user types stays in the browser's localStorage.
