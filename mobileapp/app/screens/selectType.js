import { View, Text, Image} from "react-native";
import { Divider } from "react-native-material-ui";
import { Appbar } from "react-native-paper";
import { Icon } from 'react-native-elements';
import { theme } from "../utils/theme";
import Navbar from "../components/navbar";
import { TouchableOpacity } from "react-native";
import { useNavigation } from "@react-navigation/native";

export default function Emmissions () {
    const navigation = useNavigation();
    const _navigateTo = (loc) => {
        if(loc=="Transportation")[
            navigation.navigate('SelectSub')
        ]
    }
    //1 for water, 2 for food, 3 for drinks, 4 for tobacco, 5 for vehicles, 6 for general merch, 7 for energy
    const types =[{icon:"airplane", title:"Transportation"},{icon:"fast-food", title:"Food"},{icon:"ios-wine", title:"Drinks"},
    {icon:"ios-logo-no-smoking", title:"Tobacco"},{icon:"card", title:"General"},{icon:"flash", title:"Energy"}]
    return(
        <View style={{flex:1}}>
            <Text style={{textAlign:'center', fontWeight:'bold', paddingTop:'10%', paddingBottom:'5%', fontSize:17}}>Add</Text>
            <Divider/>


            <View style={{paddingHorizontal:'5%', paddingVertical:'5%'}}>
                <Text style={{fontWeight:'bold', fontSize:15, marginBottom:'5%'}}>Select a category</Text>
                


                {types.map((type)=>(<TouchableOpacity onPress={()=>{_navigateTo(type.title)}}><View style={{alignSelf:'center', borderRadius:10, borderWidth:1, borderColor:theme.primary, padding:'2.5%', 
                backgroundColor:'#E7F3EB', flexDirection:'row', justifyContent:'flex-start', 
                width:'90%', marginBottom:'2.5%'}}>
                    <Icon name={type.icon} type="ionicon" color={theme.primary}></Icon>
                    <Text style={{fontWeight:'200', color:'#000', marginLeft:'5%', textAlignVertical:'center'}}>{type.title}</Text>
                </View></TouchableOpacity>))}


            </View>
            <Navbar/>

        </View>
    )
}