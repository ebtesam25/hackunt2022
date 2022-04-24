import { View, Text, Image} from "react-native";
import { Divider } from "react-native-material-ui";
import { Appbar } from "react-native-paper";
import { Icon } from 'react-native-elements';
import { theme } from "../utils/theme";
import Navbar from "../components/navbar";
import { TouchableOpacity } from "react-native";
import { useNavigation } from "@react-navigation/native";

export default function SelectSub () {
    const navigation = useNavigation();
    //1 for small truck, 2 for medium to large truck, 3 for passenger car, 4 for motorhome, 5 for motorcycle, 6 for vans / suvs, 7 for Bus, 8 for subway transit
    const types =[{icon:"bus",title:"Small Truck"},{icon:"bus",title:"Medium to Large Truck"},{icon:"car", title:"Car"},{icon:"bus", title:"Bus"},
    {icon:"train", title:"Train"},{icon:"home", title:"Motorhome"},{icon:"bicycle", title:"Motorbike"}]
    return(
        <View style={{flex:1}}>
            <Text style={{textAlign:'center', fontWeight:'bold', paddingTop:'10%', paddingBottom:'5%', fontSize:17}}>Add Emission</Text>
            <Divider/>


            <View style={{paddingHorizontal:'5%', paddingVertical:'5%'}}>
                <Text style={{fontWeight:'bold', fontSize:15, marginBottom:'5%'}}>Select a sub category</Text>
                


                {types.map((type)=>(<TouchableOpacity onPress={()=>{navigation.navigate('Add',{type:'Transportation',subtype:type.title, icon:type.icon})}}><View style={{alignSelf:'center', borderRadius:10, borderWidth:1, borderColor:theme.primary, padding:'2.5%', 
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