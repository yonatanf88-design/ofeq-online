# אופק — כל יום רעיון קדימה

אפליקציית למידה אישית בעברית בנושאי מצוינות תפעולית, ניהול, כספים, תעשייה וחדשנות.

## פרסום האתר (פעם אחת)
1. פתחו [Settings → Pages](https://github.com/yonatanf88-design/ofeq-online/settings/pages).
2. תחת **Build and deployment → Source** בחרו **GitHub Actions**.
3. פתחו [Actions](https://github.com/yonatanf88-design/ofeq-online/actions/workflows/publish.yml), בחרו **Run workflow**, הענף `main`, ואשרו.
4. לאחר שהרצת `Ofeq - Daily updates and publish` הסתיימה בהצלחה, האתר אמור להיות זמין:
   https://yonatanf88-design.github.io/ofeq-online/

## אוטומציה
- עדכון RSS מתוזמן מדי יום ב־07:37 לפי שעון `Asia/Jerusalem`.
- הנתונים הם כתבות חיצוניות אמיתיות (כותרת, תאריך, מקור וקישור), **לא סיכומי AI**.
- על כשל מלא בהבאת כתבות נשמר קובץ `site/feed.json` האחרון, והאתר ממשיך לעבוד.
- העדפות המשתמש נשמרות **מקומית בדפדפן**, ללא סנכרון בין מכשירים.
- הזרמת חדשות תלויה בזמינות מקורות RSS ו-GitHub Actions; אין הבטחה לשעה מדויקת.

## פרטיות
המאגר ציבורי. אין לשמור בו סיסמאות, API keys, מידע על עובדים או נתונים ארגוניים.

מדריך נוסף: [DEPLOY.md](DEPLOY.md).
