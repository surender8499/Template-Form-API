Create table templateinfo(createdby varchar(20),template_name varchar(20), template_data text not null,
Primary key(createdby,template_name))

select * from templateinfo where createdby = '1' and template_name = 'Test'

INSERT INTO public.templateinfo
(createdby, template_name, template_data)
VALUES('', '', '');

DELETE FROM public.templateinfo WHERE createdby='' AND template_name='';

UPDATE public.templateinfo SET template_data='' WHERE createdby='' AND template_name='';

select * from templateinfo

