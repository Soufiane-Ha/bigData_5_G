# bigData_5_G
> [!TIP]
> الهدف و المصدر.
<div dir="rtl">
الهدف تحميل بيانات ضخمة و تحليلها و مقارنة بين Dask , Pandas et Chunksize

قاعدة البيانات : ecommerce-behavior-data-from-multi-category-store  من موقع  kaggle
</div>

> [!TIP]
> Dask :

<div dir="rtl">


يستخدم المعالجة المتوازية ولا يحمل كل البيانات في الذاكرة مرة واحدة لتوفير استهلاك ذاكرة بل يقسمها الىpartitions
</div>

> [!TIP]
> Pandas :
> 
<div dir="rtl">

عكس  Dask لاكنه أسرع في التنفيذ
</div>

> [!TIP]
> Chunksize :
> 
<div dir="rtl">
</div>

## Comparison Table :
<div dir="rtl">


| الطريقة | السرعة      | استهلاك الذاكرة   | الأفضل متى؟              |
| ------- | ----------- | ----------------- | ------------------------ |
| Pandas  |  الأسرع   |  عالي جداً      | إذا كان RAM كبير         |
| Dask    | أبطأ قليلاً |  منخفض           | للبيانات الضخمة          |
| Chunks  | متوسط       |  لم تستفد فعلياً | فقط عند المعالجة الجزئية |
</div>

