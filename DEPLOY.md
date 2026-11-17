# מדריך תפעול לאופק

## פרסום
האתר מתפרסם ב-GitHub Pages דרך ה-workflow:
[Ofeq - Daily updates and publish](https://github.com/yonatanf88-design/ofeq-online/actions/workflows/publish.yml).

כתובת: https://yonatanf88-design.github.io/ofeq-online/

## AI — הפעלה
- צור מפתח ב-https://platform.openai.com/api-keys והגדר תקציב שימוש.
- עבור אל https://github.com/yonatanf88-design/ofeq-online/settings/secrets/actions
- לחץ **New repository secret** והוסף את `OPENAI_API_KEY`.
- אל תדביק מפתח לקוד, לצ'אט, לתיקייה ציבורית או לכתובת האתר.
- עבור ל-Actions → Ofeq - Daily updates and publish → Run workflow.
- ה-workflow מריץ בדיקות, משיכת חדשות, ואחר כך ניסיון ליצירת תובנות AI. הצלחה ביצירת תובנות אינה מובטחת בכל יום.
- אם אין מפתח, הקוד יוצא בלי לנסות ליצור תובנות חדשות. האפליקציה והחדשות ממשיכות לפעול.

## שקיפות
- למודל נשלחים רק כותרת ותיאור RSS של המפרסם, קטגוריה מקצועית כללית ותאריך; אין העברה של שמך או הנתונים שנשמרו בדפדפן.
- כל התובנות שנוצרות ונשמרות ב-GitHub הן **פומביות**.
- AI אינו קורא את המאמר המלא. התקציר מבוסס על פסקת ה-RSS הקצרה בלבד.
- היישום והמשימה הם רעיונות תרגול היפותטיים ולא עצה פיננסית אישית.
- אין לפרסם במאגר מידע ארגוני, סיסמאות או מידע מזהה של עובדים.
