import click 
'''
@click.command()
@click.option('--count', default = 1,help = 'No. of times for greeting')
@click.option('--name',prompt = 'Enter the name',help = 'Who is to be greeted')

def hello(count,name):

    for num in range(count):
        click.echo(f'Hello {name}')

if __name__ == '__main__' :
    hello()
'''

@click.command() 
@click.option('-sn','--schoolnum', default = 1 , required = True ,prompt = 'Enter the school number')

def description(schoolnum):
    
    if schoolnum == 2961 :
        @click.command() 
        @click.option('--count',default = 1,required = True,prompt = 'No. of times you want to print message')
            
        def physics(count):
            for idx in range(count):
                click.echo(f'Ajay {schoolnum} loves physics .')



if __name__ == '__main__' :
    description()               