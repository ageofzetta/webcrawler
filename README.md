
Lambda carga index.html
    leo los a tags, separo los que apuntan al mismo dominio
    se deduplican
    los guardo
        Para cada enlace repito el proceso ^

Con la base de datos de links corro mi crawler

# Para "guardar" el env

## Con conda

```
conda list -e > requirements.txt  
```

## Con pip
```
pip freeze > requirements.txt
```

# Instalar y comprimir dependencias 


Desde la raiz del proyecto

```
pip install --target ./package bs4;
cd package;
zip -r ../my-deployment-package.zip .;
cd ..;
zip -g my-deployment-package.zip lambda_function.py;
```