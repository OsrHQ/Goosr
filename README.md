# ميزان الجولة · Round Scale

حاسبة لايف لجولات **Up or Down** (طالع أو نازل) على BTC وETH وBNB: جولات 5 دقايق و15 دقيقة وساعة.

- تاخذ السعر لايف من Binance (أكثر من مرة في الثانية) وسعر البداية لكل جولة.
- تقدّر احتمال Up (طالع) وDown (نازل) من بعد السعر عن سعر البداية والوقت الباقي وحركة السوق في آخر ساعة.
- تقارن الاحتمال مع أسعار التطبيق (Predict.fun) بعد الرسوم (2%)، وتقول «ادخل» بس لما السعر أرخص من الفرصة بفرق واضح.
- سجل صفقات: يجيب نتيجة كل جولة من Binance ويحدّث الرصيد لحاله.
- قفل يومي: لو نزل الرصيد للحد اللي كتبته، «ادخل» يقفل لين 12 بالليل بتوقيت السعودية. وبعد خسارتين ورا بعض، استراحة 15 دقيقة.
- الأخبار الأمريكية (CPI، الوظائف، الفائدة): ما فيه «ادخل» في جولة ينزل فيها خبر، ولين ربع ساعة بعده.

ما تعرف وين بيروح السعر، ولا أحد يعرف. هي أداة حساب، مو توصية.

The page is a single static `index.html` (no build step). It reads public market data from `data-stream.binance.vision` (WebSocket) and `data-api.binance.vision` (REST), and, with the user's own read-only key, order books from `api.predict.fun`. Everything the user types stays in the browser's localStorage.
